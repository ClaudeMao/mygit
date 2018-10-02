from multiprocessing import Process
import os 
import time
#winsdows下无os.fork()
# fork子进程默认为 pid = 0

def run_proc(name):
    print('Run child process {}({})'.format(name, os.getpid()))
    
if __name__ == '__main__':
    print('Parent process is {}'.format(os.getpid()))
    p = Process(target = run_proc, args = ('cnbb',))
    # args 的参数只要一个值的时候，参数后面需要加一个逗号
    # 表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')