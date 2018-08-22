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
                 
