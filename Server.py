import socket
from pathlib import Path
path=Path(input("File Path:"))
tcpc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpc.bind(("0.0.0.0",8086))
tcpc.listen(1)
print("waiting for connection...")
client,(ip,port)=tcpc.accept()
print("connected!")
print("sending file...")
client.send(path.name.encode())
with path.open("rb") as data:
    try:
        for i in data:
            client.send(i)
    except Exception as error:
        print("error",error)
print("sended")
tcpc.close()