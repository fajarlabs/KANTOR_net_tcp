import getpass
import sys
import telnetlib
import socket
import threading
import serial
import time
import logging

logging.basicConfig(filename='D:/python/info.log',level=logging.DEBUG)

# SERVER
IP_SERVER = "10.1.11.37"
# Ganti PORT disini sesuai yg disediakan oleh pihak server
PORT_SERVER = 4023
# init socket server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# TELNET
HOST_TCP_CLIENT = "127.0.0.1"
PORT_TCP_CLIENT = 8000;

# SERIAL
S_COM = 'COM1'
S_BAUDRATE = 38400

def _serial_capture() :
    global S_COM
    global S_BAUDRATE
    try :
        ser = serial.Serial(port=S_COM,baudrate=S_BAUDRATE,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
        while True:
             cc=str(ser.readline())
             print(cc)
             _transmit_UDP(cc)
             #time.sleep(1)
    except Exception as e :
        print(e)
        logging.debug(str(e))

def telnet_TCP() :
    global HOST_TCP_CLIENT
    global PORT_TCP_CLIENT

    try :
        telnet = telnetlib.Telnet()
        telnet.open(HOST_TCP_CLIENT, PORT_TCP_CLIENT)
        while True:
            line = telnet.read_until("\n")  # Read one line
            print(line)
            _transmit_UDP(line)
            time.sleep(1)

    except Exception as e:
        print(str(e))
        logging.debug(str(e))

def _transmit_UDP(data) :
    global IP_SERVER
    global PORT_SERVER
    global sock
    try :
        sock.sendto(data, (IP_SERVER, PORT_SERVER))
    except Exception as e:
        print(str(e))
        logging.debug(str(e))

if __name__ == "__main__":
    while True:
        telnet_TCP()
