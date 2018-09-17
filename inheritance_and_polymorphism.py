class People(object):
    def run(self):
        print('People are running.')

class Ivy(People): #类型既为Ivy又为People，为多态
    def run(self):
        print('Ivy is running.') #当子类和父类有相同方法时，只提取子类的方法

class Claude(People):
    def run(self):
        print('Claude is running.')

def run_twice(People):
    People.run()
    People.run()

run_twice(People())
run_twice(Ivy())
run_twice(Claude())#新增的子类只需要继承父类即可使用父类的方法