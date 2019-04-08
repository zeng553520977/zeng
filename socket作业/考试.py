import socket

addr = ('0.0.0.0', 5999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)


print('服务器已启动')

while 1:
    u_input = input('请输入')
    s.send(u_input.encode())
    if len(u_input) == 1024:
        continue
    if u_input == ' ':
        s.close()
        break
    server = s.recv(1024).decode()
    print(server)

