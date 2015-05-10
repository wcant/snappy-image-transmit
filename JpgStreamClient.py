import logging
from snapconnect import snap
from PIL import Image

portalAddr = '\x00\x00\x01'

im = Image.open("pic_10q_800x600_grey.jpg")

rgbs = list(im.getdata())

h = []
for pixel in rgbs:
    h.append(chr(pixel))

def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)


class JpgStreamClient(object):
    def __init__(self):
        self.snap = snap.Snap(funcs={'sendImage' : self.send_image})
        self.log = logging.getLogger("JpgStreamClient")

    def send_image(self, h):
        
