import socket

addr = ('0.0.0.0', 1999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)


print('服务器已启动')

while 1:
    u_input = input('请输入').strip()
    s.send(u_input.encode())
    if len(u_input) == 1:
        continue
    if u_input == ' dsada':
        s.close()
        break
    server = s.recv(1024).decode()
    print(server)


