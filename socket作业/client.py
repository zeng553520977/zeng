import socket
import os

dir_name = os.path.dirname(__file__)
jpg_name = os.path.join(dir_name,'3_1.png')
jpg_name1 = os.path.join(dir_name,'3_1_copy1.jpeg')

with open(jpg_name,'rb') as f:
    b_file = f.read()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('127.0.0.1', 60000)

ss.connect(addr)

ss.sendall(b_file)

ss.close()