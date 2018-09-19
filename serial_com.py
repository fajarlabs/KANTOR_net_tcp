import serial
import time
from udp_sender import transmit_udp

# SERIAL
S_COM = 'COM1'
S_BAUDRATE = 38400

def serial_capture() :
    global S_COM
    global S_BAUDRATE
    try :
        ser = serial.Serial(port=S_COM,baudrate=S_BAUDRATE,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
        while True:
             cc=str(ser.readline())
             print(cc)
             transmit_udp(cc)
             time.sleep(1)
    except Exception as e :
        print(e)

if __name__ == "__main__":
	serial_capture()