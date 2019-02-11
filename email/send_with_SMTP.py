from email.mime.text import MIMEText
text = input('input messages:')
msg = MIMEText(text,'plain','utf-8')

from_addr = input('From:')
password = input('Password:')

to_addr = input('To:')

smtp_server = input('SMTP server:')

import smtplib
server = smtplib.SMTP(smtp_server, 587) #465 or 587 for tencent smtp
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
