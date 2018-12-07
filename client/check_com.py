import serial
import time

# SERIAL
S_COM = 'COM1'
S_BAUDRATE = 38400

def serial_connect() :
    global S_COM
    global S_BAUDRATE
    try :
        ser = serial.Serial(port=S_COM,baudrate=S_BAUDRATE,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
        while True:
             cc=str(ser.readline())
             print(cc)
             time.sleep(0.01)
    except Exception as e :
        print(e)

if __name__ == "__main__":
	serial_connect()