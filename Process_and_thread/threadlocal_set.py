import threading

# 创建一个全局ThreadLocal对象
local_school = threading.local()
# 常用ThreadLocal绑定数据库连接，方便每个线程调用
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Claude',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Ivy',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()