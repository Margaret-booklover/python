import socket

HOST = '127.0.0.1'
PORT = 50007
flag = False
while not flag:
    mail = input("Your e-mail: ")
    message = input("Your message: ")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(mail.rjust(1024, " ").encode())
            s.sendall(message.rjust(1024, " ").encode())
            data = s.recv(1024)
        if data.decode() == "OK":
            print('Received your feedback. Thank you!')
            flag = True
        else:
            print(data.decode())
            flag = False
    except Exception as e:
        print(e)
