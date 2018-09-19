import socket

# SERVER
IP_SERVER = "10.1.11.37"
PORT_SERVER = 4023
# init socket server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def transmit_udp(data) :
    global IP_SERVER
    global PORT_SERVER
    global sock
    try :
        sock.sendto(data, (IP_SERVER, PORT_SERVER))
    except Exception as e:
        print(str(e))