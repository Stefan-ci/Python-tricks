import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(f"Your device name is: {hostname} and your device IP address is: {IP}")
