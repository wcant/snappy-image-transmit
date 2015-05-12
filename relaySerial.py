from synapse.switchboard import *

portalAddr = "\x00\x00\x01" # <= put the address of the OTHER node here

@setHook(HOOK_STARTUP)
def startupEvent():
    initUart(1, 9600) # <= put your desired baudrate here!
    flowControl(1, False) # <= set flow control to True or False as needed
    crossConnect(DS_UART1, DS_TRANSPARENT)
    ucastSerial(portalAddr)
