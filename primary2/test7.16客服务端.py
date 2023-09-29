import socket
socket_server=socket.socket()
socket_server.bind(("localhost", 8888))
socket_server.listen(1)

conn,address=socket_server.accept()
print(f'{address}')
while True:
    data:str=conn.recv(1024).decode("UTF-8")
    print(f'{data}')
    msg=input("reponed:")
    if msg=='exit':
        break
    conn.send(msg.encode("UTF-8"))

conn.close()
socket_server.close()



























