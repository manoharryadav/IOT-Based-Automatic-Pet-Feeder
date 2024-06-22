import serial
import time
data = serial.Serial(
                    'COM5',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )

def Send(a):
  data.write(str.encode(a))
  print('sent............')

def Read():
  Data = data.read(1)
  Data = Data.decode('utf-8', 'ignore')
  return Data
