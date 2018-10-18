import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()
# 此处用encode将str转化为bytes类型
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = 'sadness'.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    MD5PASSWORD_in_hmac = hmac_md5(user.key, password)
    if MD5PASSWORD_in_hmac == user.password:
        print('login sucessfully')
    else:
        print('Invalid username or password')

login('michael','123456')
login('bob', 'abc999')
login('alice', 'alice2008')