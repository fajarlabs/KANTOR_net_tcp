import telnetlib
import time
from udp_sender import transmit_udp

# TELNET
HOST_TCP_CLIENT = "127.0.0.1"
PORT_TCP_CLIENT = 8000;

def telnet_start() :
    global HOST_TCP_CLIENT
    global PORT_TCP_CLIENT

    try :
        telnet = telnetlib.Telnet()
        telnet.open(HOST_TCP_CLIENT, PORT_TCP_CLIENT)
        while True:
            line = telnet.read_until(b"\n")  # Read one line
            print(str(line, 'utf-8'))
            #transmit_udp(line)
            time.sleep(5)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    telnet_start()  