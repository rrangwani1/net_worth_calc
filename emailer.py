import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

'''
msg = MIMEText(fp.read())
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
'''



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