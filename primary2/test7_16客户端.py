import socket

socket_client=socket.socket()

socket_client.connect(("localhost", 8888))
while True:
    msg=input("msf:")
    if msg=='exit':
        break
    socket_client.send(msg.encode("UTF-8"))
    recv_data=socket_client.recv(1024)
    print(f"responed:{recv_data.decode('UTF-8')}")

socket_client.close()









