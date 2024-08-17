import socket
from pathlib import Path
from sys import exit
def fexit(tcpc):
    tcpc.close()
    exit()
tcpc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input("sender ip:")
tcpc.connect((ip,8086))
file=tcpc.recv(1000000).decode()
path=Path(file)
with path.open("ab") as rfile:
    while True:
        data=tcpc.recv(1000000)
        if data.decode("ANSI"):
            rfile.write(data)
        else:
            fexit(tcpc)
    tcpc.close()
    exit()
print("successfully!")