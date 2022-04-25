# from curses import baudrate
import os 
import time
from datetime import datetime 
from serial import Serial 

import serial

s = serial.Serial(port = 'COM3', baudrate=19200, bytesize = 8, timeout = 1)

s.write(str.encode('8.'))


# 0: dừng
# 1: thẳng
# 2: lùi
# 3: rẽ trái
# 4: rẽ phải
# 5: đi ngang qua trái
# 6: đi ngang qua phải
# 7: lùi trái 
# 8: lùi phải

# 0: dừng
# 1: khong lam gi
# 2: thang
# 3: ngang trai
# 4: ngang phai
# 5: xoay phai
# 6: xoay trai
# 7: lui
# 8: khong lam gi