import smtplib
from email.header import Header
from email.mime.text import  MIMEText


class EmailUtils:
    @staticmethod
    def send_from_gmail_to_my_workemail(subject, msg):
        gmail_host = 'smtp.gmail.com'
        gmail_port = 587
        gmail_user = 'max21011985@gmail.com'
        gmail_pass = 'vkytotambbyezpjm'
        mail_sender = gmail_user
        mail_receivers = ['sumx@iata.org']

        msg_plain = 'Email Content'
        message = MIMEText('Email Content','plain', 'utf-8')

        message['From'] = mail_sender
        message['To'] = mail_receivers
        message['Subject'] = Header(subject)

        try:
            server = smtplib.SMTP(gmail_host, gmail_port)
            server.ehlo()
            server.starttls()
            server.login(gmail_user,gmail_pass)
            server.sendmail(mail_sender,mail_receivers,msg)
            print('success!')
        except smtplib.SMTPException as ex:
            print('error', ex)



