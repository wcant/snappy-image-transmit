
#This version works fine on my mac.  Using cu.usbserial instead of tty.usbserial
# works

import logging
from snapconnect import snap
class McastCounterClient(object):
    def __init__(self):
        # Create a SNAP instance
        self.snap = snap.Snap(funcs={'setButtonCount': self.set_button_count}) # Open COM1 (port 0) connected to a serial SNAP bridge 
        self.snap.open_serial(snap.SERIAL_TYPE_RS232, '/dev/cu.usbserial' )
        #Accept connection from other SNAP connect instances and Portal
        self.snap.accept_tcp()

        # Create a logger
        self.log = logging.getLogger("McastCounterClient")

    def set_button_count(self, count):
        # This function is called by remote SNAP nodes
        # Log the current count received
        self.log.info("The button count = %i" % (count))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # print logging messages to STDOUT 
    client = McastCounterClient() # Instantiate a client instance 
    client.snap.loop() # Loops waiting for SNAP messages
