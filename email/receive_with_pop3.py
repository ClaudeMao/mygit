import poplib

email = input('Email address:')
password = input('Password:')
pop3_server = input('pop3 server:')

server = poplib.POP3(pop3_server)

server.set_debuglevel(1)

print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Messages:{} . Size:{}'.format(server.stat()))

resp, mails, octets = server.list()

print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg = Parser().parsestr(msg_content)

server.quit()
