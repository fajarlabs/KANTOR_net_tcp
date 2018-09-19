import socket
from threading import Thread
import time


TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
MS_INTERVAL = 0.5 # setengah detik

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

def handle_client_connection() :
    conn, addr = s.accept()
    print ('Connection address:', addr)
    while True:
        data = conn.recv(BUFFER_SIZE)
        conn.send(data)  # echo
    conn.close()

if __name__ == "__main__":
    while True:
        try :
            t = Thread(target=handle_client_connection)
            t.setDaemon(True)
            t.start()
            time.sleep(MS_INTERVAL)
        except Exception as e :
            print(e)