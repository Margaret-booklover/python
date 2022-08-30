import email
import imaplib
import os
from email.header import decode_header
from time import sleep

from dotenv import load_dotenv


HOST = '127.0.0.1'
PORT = 50007
load_dotenv()

my_mail = os.getenv('EMAIL_LOGIN')
my_password = os.getenv('EMAIL_PASSWORD')
imap_host = os.getenv('IMAP_HOST')
imap_port = os.getenv('IMAP_PORT')
check = os.getenv('PERIOD_CHECK')

imap = imaplib.IMAP4_SSL(imap_host)
imap.login(my_mail, my_password)
while True:
    status, messages = imap.select("INBOX/ToMyself")
    messages = int(messages[0])
    for i in range(messages+1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                email_message = {
                    part.get_content_type(): part.get_payload()
                    for part in email.message_from_bytes(response[1]).walk()
                }
                body = email_message["text/plain"][:-304]
                subject = str(subject)
                with open("IDnumbers.txt", "r") as f:
                    mas = [str(row)[:-1] for row in f]
                    if subject in mas:   # если номер уникальный и содержится в базе уникальных номеров
                        with open("success_request.log", "r") as file:
                            mas1 = [row.split(':', 1)[0] for row in file]
                        if subject in mas1:
                            pass  # если номер уже содержится в базе, значит мы это письмо смотрели, ничего не делаем
                        else:  # a если его еще нет в файле успешно обработанных запросов
                            with open("success_request.log", "a") as file:
                                file.write(subject+": "+body)
                    else:   # если тема письма какая-то другая, то записываем в файл ошибок
                        with open("error_request.log", "r") as file:
                            mas1 = [row.split(':', 1)[0] for row in file]
                        if subject in mas1:
                            pass  # если номер уже содержится в базе, значит мы это письмо смотрели, ничего не делаем
                        else:  # a если его еще нет в файле успешно обработанных запросов
                            with open("error_request.log", "a") as file:
                                file.write(subject+": "+body)
    print("Mailbox check passed successfully")
    sleep(float(check))
