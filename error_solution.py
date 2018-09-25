from functools import reduce
import logging

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        logging.exception(e) #记录错误日志
    else:
        print('No error!')
    finally:
        return float(s)
        
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)
    #匿名函数接受两个参数：acc和x，表达式为对两个求和，reduce表示其作用在ns列表上
def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r) 
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
