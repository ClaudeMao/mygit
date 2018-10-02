from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task {} ({})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task {} runs {} seconds.'.format(name, (end - start)))
    
if __name__ == '__main__':
    print('Parent process {}'.format(os.getpid()))
    p = Pool(8) #创建8个子进程 表示进程池中最多有8个一起执行
    for i in range(50):
    # 创建50个任务 注意：如果添加的任务数量超过了进程池中进程的个数的话
    # 那么就不会接着往进程池中添加，如果还没有执行的话，他会等待前面的进程结束
        p.apply_async(long_time_task, args = (i,)) #哪个先结束就先输出谁 用apply是等待上一个任务结束才输出下一个
    print('waiting for all subprocesses done...')
    p.close() #Pool要先调用close close之后不能添加新的Process
    p.join() # 主进程在这里等待，只有子进程全部结束之后，在会开启主线程
    print('All subprocesses done.')