class Animal(object):
    pass
    
class RunnableMixIn(object): #带MixIn表示为额外的继承关系
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class Mammal(Animal):
    pass
    
class Bird(Animal):
    pass
    
class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal,FlyableMixIn):
    pass

class Parrot(Bird,FlyableMixIn):
    pass

class Ostrich(Bird, RunnableMixIn):
    pass
    
