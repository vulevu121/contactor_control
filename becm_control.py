#!/usr/bin/python3
""" Author: Khuong Nguyen, Vu Le, Tai Le
    Script for controlling 2.0  BECM"""


import can
import can.interfaces
from can.interface import Bus
from can import Message
import time
import subprocess
import datetime
import numpy as np

######## CAN ID ################
TRAC_BATT_COMMAND_ID = 0x230
TRAC_BATT_STATUS_1_ID = 0x235

####### Miscellaneous #######
bus = None

##################################### BECM Class definition ############################################
class BECM:
    def __init__(self):
        
        # Initilize signals
        self.ACChargingActv = 0x0     # bit 7 of byte 0
        self.DCChargingActv = 0x0     # bit 6 of byte 0
        self.ACContactorCmd = 0x0     # bit 5 of byte 0
        self.ContactorCmd   = 0x1     # bit 2,3,4 of byte 0. 1 is restricted open
        self.Counter        = 0x0     # bit 0,1 of byte 0. min: 0, max:3 
        self.DCContactorCmd = 0x0     # bit 7 of byte 1
        self.BECM_NM        = 0x0     # bit 6,5 of byte 1
        self.TB_Status      = "None"
        self.HV_Current     = 9999
#################################   BECM methods ########################################################
    def update_CAN_msg(self):
        self.Counter = (self.Counter + 1) % 4
        
        byte0 = (self.ACChargingActv << 7) | (self.DCChargingActv << 6)\
                | (self.ACContactorCmd << 5) | (self.ContactorCmd << 2) | self.Counter
                
        byte1 = (self.DCContactorCmd << 7) | (self.BECM_NM << 6)
        
        self.ContactorCmdMsg = can.Message(arbitration_id = TRAC_BATT_COMMAND_ID,extended_id = False, data=[byte0,byte1])

        # add CAN message to list
        self.msg_list = []
        self.msg_list = [self.ContactorCmdMsg]

    def readStatus(self,bus):
        while(True):
            startTime = time.time()
            # assume CAN traffic always present
            msg = bus.recv()        
            if msg.arbitration_id == TRAC_BATT_STATUS_1_ID:
                self.TB_Status = self.decode_tb_status((msg.data[1] >> 1) & 0xF)
                self.HV_Current = ((msg.data[0] << 3) | (msg.data[1] >> 5)) - 1000
                # too many message queued up
                #print(self.TB_Status)
                bus.flush_tx_buffer()
                
            if time.time() - startTime > 0.5:
                break            
                    
        
    def restrictedOpen(self):
        self.ContactorCmd = 0x1

    def restrictedClose(self):
        self.ContactorCmd = 0x3

    def disableBECM(self,bus):
        self.restrictedOpen()
        startTime = time.time()

        while(True):
            self.update_CAN_msg()
            for msg in self.msg_list:
                bus.send(msg)
            time.sleep(0.025)
            if time.time() - startTime > 1:
                break

    def decode_tb_status(self,status):                                     # Pass status signal in as argument
        status2str = {0x0: 'NO FAULT',
                      0x1: 'WARNING',
                      0x2: 'CHARGER DISABLED',
                      0x3: 'LIMP HOME HIGH',
                      0x4: 'LIMP HOME LOW',
                      0x5: 'LIMP HOME LOW NO RESTART',
                      0x6: 'EPO REQUEST',
                      0x7: 'SOFT EPO',
                      0x8: 'HARD EPO',
                      }
        
        try:
            return status2str[status]
        except:
            return 'Not Available'
            

#################################   BECM methods END ########################################################

def limit(num,min,max):                 #limit range for torque command or any other command
    if num < max and num > min:
        return num
    elif num < min:
        return min
    elif num > max:
        return max



def getByte(sourceByte, sourceIdxRange, destByte, destIdxRange):
    
    def getBit(val, bit):
        return (int((val & (1 << bit)) != 0))

    def setBit(byte, bit, bitval):
        if bitval == 1:
            return (byte | (1 << bit))
        else:
            return (byte & ~(1 << bit))

    
    for s, d in zip(sourceIdxRange, destIdxRange):
        destByte = setBit(destByte, d, getBit(sourceByte, s))

    return destByte


def initCAN():
        global bus
        can.rc['interface'] = 'socketcan'
        can.rc['bitrate'] = 500000
        can.rc['channel'] = 'can0'
        bus = Bus()
        bus.flush_tx_buffer()


if __name__ == "__main__":
    initCAN()
    becm = BECM()


    ######## Test enable/disable  ################
    while True:
        becm.update_CAN_msg()
        bus.send(becm.ContactorCmdMsg)
        print(becm.ContactorCmdMsg)
        time.sleep(2)
                 
