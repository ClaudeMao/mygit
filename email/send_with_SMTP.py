from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From:')
password = input('Password:') #input authorization code but not login password
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('You are so damn beautiful','plain','utf-8')
msg['From'] = _format_addr('Adam <{}>'.format(from_addr))
msg['To'] = _format_addr('piggy <{}>'.format(to_addr))
msg['Subject'] = Header('greeting from smtp','utf-8').encode()

server = smtplib.SMTP(smtp_server, 587) #465 or 587 for tencent/google smtp
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()