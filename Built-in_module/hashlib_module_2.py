import hashlib, random
'''
db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
'''
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = 'sadness'.join([chr(random.randint(48, 122)) for i in range(20)])
        # 在类中加了盐 后面需要回来取
        self.password = get_md5(password + self.salt + username)
        # 加密方式为密码加盐加用户名
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    MD5PASSWORD = get_md5(password + user.salt + username)
    if MD5PASSWORD == user.password:
        print('login sucessfully')
    else:
        print('Invalid username or password')

login('michael','123456')