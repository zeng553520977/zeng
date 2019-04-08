import socket
Addr = ('0.0.0.0',5999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(Addr)
s.listen(10)
conn, addr = s.accept()
print('服务器已启动')
while 1:
    data = conn.recv(1024).decode()
    print(data)
    user_input = input('请输入')
    conn.send(user_input.encode())


