clientServer = '127.0.0.1'
PORT = 65432
if clientServer and PORT == True:
    import socket
    HOST = '127.0.0.1'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
else:
     print('connection dropped)')




