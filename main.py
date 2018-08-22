from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtGui import QIcon, QPixmap
import sys

from ContactorControl_gui import *
from becm_control import *
import threading
import re

TransmitFlag = False
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
        self.startBtn.clicked.connect(lambda: self.start_CAN_thread())
        self.stopBtn.clicked.connect(lambda: self.stop_transmit())
        self.openContactorBtn.clicked.connect(lambda: self.openContactor())
        self.closeContactorBtn.clicked.connect(lambda: self.closeContactor())

    def openContactor(self):
        print("Open Contactor...")
        self.becm.restrictedOpen()

    def closeContactor(self):
        print("Close Contactor...")
        self.becm.restrictedClose()

    def start_transmit(self):
        print("Start CAN transmit...")
        global TransmitFlag
        global bus
        global EnableFlag 
       
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
        

        # Set this flag to stop the ongoing transmittion
        
        TransmitFlag = False
        # transmit 1 more second before stopping CAN
        print ("Disable BECM...")
        self.becm.disableBECM(bus)
        print ("Stop CAN transmit...")

    def start_CAN_thread(self):
        print ("Start CAN thread...")
        global TransmitFlag
        TransmitFlag = True
        
        # separate thread to prevent gui freezing. PASS HANDLE NOT FUNCTION CALL
        thread = threading.Thread(target=self.start_transmit, args=())
        thread.daemon = True
        thread.start()        


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
    bus.flush_tx_buffer()
	
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
