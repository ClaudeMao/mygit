import itertools

def pi(N):
    # 计算pi值
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1,2)# 后一个参数为步长
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    N_odd  = itertools.takewhile(lambda x: x<=2*N, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    num = map(lambda x: 4/x if x%4==1 else -4/x, N_odd)# 用map对N_odd进行有条件操作
    # step 4: 求和:
    pi  = sum(num)
    print(pi)

pi(10)
pi(100)
pi(1000)
pi(10000)
pi(100000)
pi(1000000)