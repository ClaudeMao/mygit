import hashlib
# hashlib中提供常见的摘要算法
'''
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())
'''
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if user in db.keys():
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        md5Code = md5.hexdigest()
        if db[user] == md5Code:
            print('login successfully')
        else:
            print('Incorrect Password')
    else:
        print('Nonexisting user')

login('michael', '123456')