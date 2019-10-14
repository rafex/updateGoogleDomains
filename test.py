import socket

addr1 = socket.gethostbyname_ex('rafex.dev')

print(addr1[2][0])
