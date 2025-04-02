#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header    import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL, SMTP
from os import environ

EMAIL_HOST_USER = environ.get('SMTP_MAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environ.get('SMTP_MAIL_HOST_PASSWORD')



# provide credentials
login = EMAIL_HOST_USER
password = EMAIL_HOST_PASSWORD

# create message
msg = MIMEText('The best example! Your application works!', 'plain', 'utf-8')
msg['Subject'] = Header('Hello world', 'utf-8')
msg['From'] = login
msg['To'] = ', '.join([login, ])

# send it
s = SMTP(host='smtp.mail.ru', port=2525, timeout=10) #NOTE: no server cert. check
s.set_debuglevel(0)
try:
    s.starttls()
    s.login(login, password)

    s.sendmail(msg['From'], msg['To'], msg.as_string())
finally:
    s.quit()