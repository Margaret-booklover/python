import os
import random
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


HOST = '127.0.0.1'
PORT = 50007
load_dotenv()

my_mail = os.getenv('EMAIL_LOGIN')
my_password = os.getenv('EMAIL_PASSWORD')
mail_host = os.getenv('SMTP_HOST')
mail_port = os.getenv('SMTP_PORT')

mail2 = "irinkagolubeva.com@gmail.com"
mail3 = "margarita11072002@yandex.ru"
mail4 = "durtanan@gmail.com"

server = smtplib.SMTP(mail_host, mail_port)  # Создаем объект SMTP
server.starttls()  # Начинаем шифрованный обмен по TLS
server.login(my_mail, my_password)  # Получаем доступ
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            mail = conn.recv(1024).decode().strip()
            message = conn.recv(1024).decode().strip()
            if not mail or not message:
                break
            if '@' not in mail:
                conn.sendall("Incorrect e-mail!".encode())
                break
            else:
                conn.sendall("OK".encode())
            with open("IDnumbers.txt", "r") as f:
                mas = [int(row) for row in f]
                ID = str(random.randint(1, 1000000000))
                while ID in mas:
                    ID = str(random.randint(1, 1000000000))
            msg = MIMEMultipart()  # Создаем сообщение
            msg['From'] = my_mail  # Адресат
            msg['To'] = my_mail  # Получатель
            msg['Subject'] = str(ID)  # Тема сообщения
            msg.attach(MIMEText(message))  # Добавляем в сообщение текст
            server.send_message(msg)  # Отправляем сообщение

            msg1 = MIMEMultipart()  # Создаем сообщение
            msg1['From'] = my_mail  # Адресат
            msg1['To'] = mail  # Получатель
            msg1['Subject'] = str(ID)  # Тема сообщения
            msg1.attach(MIMEText("В теме письма - ваш ID заявки"))  # Добавляем в сообщение текст
            server.send_message(msg1)  # Отправляем сообщение

            with open("IDnumbers.txt", "a") as f:
                f.write(ID)
                f.write("\n")

            server.quit()
