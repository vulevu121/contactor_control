from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtGui import QIcon, QPixmap
import sys

from ContactorControl_gui import *
from becm_control import *
import threading
import re

TransmitFlag = False
ReadFlag = False
bus = None
cycle_time = 0.01


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
       
        # Start CAN bus
        initCAN()
        # Create BECM object
        self.becm = BECM()

        # Event handlers
        #self.startBtn.clicked.connect(lambda: self.start_CAN_thread())
        #self.stopBtn.clicked.connect(lambda: self.stop_transmit())
        
        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())
        
        self.openContactorBtn.clicked.connect(lambda: self.openContactor())
        self.closeContactorBtn.clicked.connect(lambda: self.closeContactor())

    def openContactor(self):
        print("Open Contactor...")
        self.becm.restrictedOpen()

    def closeContactor(self):
        print("Close Contactor...")
        self.becm.restrictedClose()

    def start_read(self):
        print("Reading BECM status...")
        global ReadFlag
        global bus

        while(ReadFlag):
            self.becm.readStatus(bus)
            self.tbStatusBox.setText(self.becm.TB_Status)
            self.HVCurrentBox.setText('{} A'.format(self.becm.HV_Current))
            self.MaxCellTempBox.setText('{} C'.format(self.becm.MaxCellTemp))
            
            
    def start_transmit(self):
        print("Start CAN transmit...\n")
        global TransmitFlag
        global bus
              
        # Send CAN continously
        while(TransmitFlag):
            self.becm.update_CAN_msg()
            for msg in self.becm.msg_list: 
                bus.send(msg)                
            # Send messages every 25 ms    
            time.sleep(0.025)

    def stop_transmit(self):
        global TransmitFlag
        global EnableFlag
        global ReadFlag


        # change SSB text to START
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.start_CAN_thread())
        self.startStopBtn.setText('Start')

        # Set this flag to stop the ongoing transmittion
        TransmitFlag = False
        # Set this flag to stop reading
        ReadFlag = False
        # transmit 1 more second before stopping CAN
        print ("Disable BECM...")
        self.becm.disableBECM(bus)
        print ("Stop CAN transmit...")

    def start_CAN_thread(self):
        print ("Start CAN thread...")
        global TransmitFlag
        TransmitFlag = True

        global ReadFlag
        ReadFlag = True

        # change SSB text to STOP
        self.startStopBtn.clicked.disconnect()
        self.startStopBtn.clicked.connect(lambda: self.stop_transmit())
        self.startStopBtn.setText('Stop')
        
        # separate thread to prevent gui freezing. PASS HANDLE NOT FUNCTION CALL
        send_thread = threading.Thread(target=self.start_transmit, args=())
        send_thread.daemon = True
        send_thread.start()        

        # separate thread to prevent gui freezing. PASS HANDLE NOT FUNCTION CALL
        read_thread = threading.Thread(target=self.start_read, args=())
        read_thread.daemon = True
        read_thread.start()   

def numberFromString(string):
    # this return a list of number from the string
    numbers = re.findall('\d+',string)
    # convert to integer
    numbers = [int(num) for num in numbers]
    # just need to access the first item
    return numbers[0]                

def initCAN():
    global bus
    can.rc['interface'] = 'socketcan'
    can.rc['bitrate'] = 500000
    can.rc['channel'] = 'can0'
    bus = Bus()
    #listener = Listener()
    bus.flush_tx_buffer()
	
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
