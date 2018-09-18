class Engine(object):
    def __init__(self):
        self.speed = 2
        self.__acceleration = 10
        self.__mass__ = 12
    def accelerate(self):
        return self.speed * self.speed

eng = Engine()
print(hasattr(eng, 'speed'))     #检查是否有speed属性
print(eng.speed)

print(hasattr(eng, 'acceleration'))
print(hasattr(eng, '__acceleration')) #私有变量无法使用hasattr()方法访问
print(hasattr(eng, '__mass__')

print(hasattr(eng, 'original_speed')

setattr(eng, 'original_speed', 0) #设置一个original_speed属性
eng.original_speed = 0
getattr(eng, 'original_speed')