from socket import *

client = socket(family=AF_INET,type=SOCK_STREAM)
client.connect(('localhost',8080))

while True:
    enter = input('>>>:').strip()
    if not enter:continue
    client.send(enter.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
