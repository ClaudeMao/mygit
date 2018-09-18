import functools
int15 = functools.partial(int, base = 15)
#创建偏函数时还可以接受函数对象、*args和**kw
print(int15('123456'))