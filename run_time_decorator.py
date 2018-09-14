from time import clock
import functools
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
def run_time(text):
    def decorator(func):
        @functools.wraps(func)    #此处相当于 wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print('“ {}, Current Function”:{}, Run time:{}s'.format(text,func.__name__ ,clock()))
            return func(*args, **kw) #不加此句或者不加括号内的通畅运行的话会无法实现printt调用
        return wrapper
    return decorator
@run_time('cnbb') #括号中为装饰器参数，不带参数的话只用两层嵌套
def printt():
    print('你妈死了')

printt()
print(printt.__name__)