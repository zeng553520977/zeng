import socket
HostPort = ('0.0.0.0',1999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HostPort)
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024).decode()
    print(data)
    user_input = input('请输入')
    conn.send(user_input.encode())



