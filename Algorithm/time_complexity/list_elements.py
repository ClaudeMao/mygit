import time

def test1(n): #最差且所需时间远大于其他三种，时间复杂度最高
    lst = []
    for i in range(n*10000):
        lst = lst + [i]
    return lst

def test2(n): #第三
    lst = []
    for i in range(n*10000):
        lst.append(i)
    return lst

def test3(n): #第二好
    return [i for i in range(n*10000)]

def test4(n): #最优
    return list(range(n*10000))

if __name__ == '__main__':
    time.clock()
    test4(10)
    print('time used:{}s'.format(time.clock()))
