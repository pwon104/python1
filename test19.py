import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "pwon104@gmail.com" # gmail address
gmail_pwd = "" # gmail password

def send_gmail(to, subject, text, attach):
msg = MIMEMultipart()
msg['From'] = 'pwon104@gmail.com'
msg['To'] = 'x88dufckx@naver.com'
msg['Subject'] = 'test19.py'
msg.attach(MIMEText(contents,_charset='euc-kr'))
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
mailServer = smtplib.SMTP("smtp.gmail.com", 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg.as_string())
mailServer.close()

hap,i = 0, 0

for i in range(1,101) :
    if i % 3 == 0 :
        continue
    hap += i

print("1~100의 합계(3의 배수 제외) : %d" % hap)


