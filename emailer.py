import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import config
from os.path import basename


class Emailer:

    def __init__(self):
        self.sender = config.TO_EMAIL
        self.recipient = config.FROM_EMAIL
        self.msg = MIMEMultipart('alternative')

    def create_email(self, rating, percent, inc):
        self.msg['Subject'] = config.EMAIL_SUBJECT
        self.msg['From'] = config.FROM_EMAIL
        self.msg['To'] = config.TO_EMAIL

        self.contents = config.EMAIL_CONTENTS.format(rating=rating, percent=percent, inc=inc)

        body = MIMEText(self.contents,'html')
        self.msg.attach(body)

        with open(config.GRAPH_FILE_NAME, "rb") as file:
            attach_image = MIMEApplication(
                file.read(),
                Name = basename(config.GRAPH_FILE_NAME)
            )
        attach_image['Content-Disposition'] = 'attachment; filename="%s"' % basename(config.GRAPH_FILE_NAME)
        self.msg.attach(attach_image)

    def send_email(self):
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(config.FROM_EMAIL, config.EMAIL_PASS)
        s.send_message(self.msg)
        s.quit()