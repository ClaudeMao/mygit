import base64
# base64编码原理：https://blog.csdn.net/zhubaoJay/article/details/72957135
'''
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# 标准base64编码后可能出现+和/，在URL中不能直接作为参数
# urlsafe将+和/转化为-和_
print(base64.urlsafe_b64decode('abcd--__'))
'''
def safe_base64_decode(s):
    if len(s)%4 !=0:
        