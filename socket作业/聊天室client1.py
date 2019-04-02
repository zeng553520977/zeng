import socket

hostport = ('0.0.0.0', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(hostport)

while 1:
    user_input = input('>>> ').strip()
    s.send(user_input.encode('utf-8'))
    if len(user_input) == 0:
        continue
    if user_input == 'quit':
        s.close()
        break
    server_reply = s.recv(1024).decode()
    print(server_reply)
