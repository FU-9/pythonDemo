from socket import *
from multiprocessing import Process

HOST_PORT = ('localhost',8080)

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionError:
            break
    conn.close()

if __name__ == '__main__':
    server = socket(family=AF_INET,type=SOCK_STREAM)
    server.bind(HOST_PORT)
    server.listen(5)

    while True:
        conn,addr = server.accept()
        p = Process(target=talk,args=(conn,))
        p.start()
    server.close()
