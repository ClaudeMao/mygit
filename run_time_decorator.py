from time import clock
clock()
'''
def run_time(func):  
    def wrapper(*args, **kw):
	    print('“Current Function”:{}, Run time:{}s'.format(func.__name__ ,clock()))
    return wrapper

def run_time(func):  
    def wrapper(*args, **kw):
	    print('“Current Function”:{}, Run time:{}s'.format(func.__name__ ,clock()))
        return func
    return wrapper
'''
def run_time(func):
    def wrapper(*args, **kw):
        print('“Current Function”:{}, Run time:{}s'.format(func.__name__ ,clock()))
        return func(*args, **kw) #不加此句或者不加括号内的通畅运行的话会无法实现printt调用
    return wrapper

@run_time
def printt():
    print('你妈死了')

printt()
