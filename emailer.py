import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config


class Emailer:

    def __init__(self):
        self.sender = config.TO_EMAIL
        self.recipient = config.FROM_EMAIL
        self.msg = MIMEMultipart('alternative')

    def create_email(self):
        self.msg['Subject'] = config.EMAIL_SUBJECT
        self.msg['From'] = config.FROM_EMAIL
        self.msg['To'] = config.TO_EMAIL

        body = MIMEText(config.EMAIL_CONTENTS,'html')
        self.msg.attach(body)

    def send_email(self):
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(config.FROM_EMAIL, config.EMAIL_PASS)
        s.send_message(self.msg)
        s.quit()