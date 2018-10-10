import re
mail_0 = 'someone@163.com'
mail_1 = 'claudemao0131@gmail.com'



def is_valid_email(addr):
    if re.match('^([a-zA-Z]+)|([0-9]+)\@([a-zA-Z]+)\.com', addr):
        return 0
    else:
        return -1

def name_of_email(addr):
    re_mail = re.compile('^([a-zA-Z]+)|([0-9]+)\@([a-zA-Z]+)\.com$')
    # 重复使用的话预编译该正则表达式（提高效率）
    if is_valid_email(addr) == 0:
        print(re_mail.match(addr).group(0))
    else:
        print('Invalid email')

if __name__ == '__main__':
    print(is_valid_email(mail_0))
    name_of_email(mail_0) 
    print(is_valid_email(mail_1))
    name_of_email(mail_1)