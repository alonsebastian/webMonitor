# -*- encoding: utf-8 -*-
#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

f = open ("conf/user", "r")
gmail_user = f.read()
gmail_user = gmail_user.replace('\n','')
f.close()

f = open ("conf/pwd", "r")
gmail_pwd = f.read()
gmail_pwd = gmail_pwd.replace('\n','')
f.close()

def mail(to, subject, text, attach0=None):

    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    if attach0:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach0, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach0))
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

if __name__ == '__main__':
    mail("alon.sebastian@gmail.com",
   "Hello from python!",
   "Email sent from python")
