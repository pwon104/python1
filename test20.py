import smtplib

from email.message import EmailMessage
# 계산식 시작
i,hap = 0,0

for i in range(1,100):
   if i % 3 == 0:
       continue
   hap += i
# print('1~100의 합계(3의 배수 제외) : %d'%hap)
# 계산식 끝
msg = EmailMessage()
msg['Subject'] = '안녕하세요.'
msg['From'] = 'park@passme.kr'
msg['To'] = 'park@passme.kr'
msg['Body'] = ''

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

