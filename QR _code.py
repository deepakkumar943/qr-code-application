
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *

  
s = "www.github.com/deepakkumar943 "

url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)


