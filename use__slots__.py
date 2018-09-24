from types import MethodType
# original method 
class Student(object):
    pass
    
    def set_age(self, age):
        self.age = age

s = Student()
s.name = 'Claude'
print(s.name)
s.set_age(25)
print(s.age)

# to add a new method when programme is running:
def set_score(self, score):
    self.score = score
b = Student()
b.name = 'Ivy'
print(b.name)

b.set_score = MethodType(set_score, b)
b.set_score(88)
print(b.score)

# to restrict property defined in substance
class Student2(object):
    __slots__ = ('name','age')
    
a = Student2()
a.name = 'Claude'
a.age = 25
# a.score = 99 This won't run because property was restricted
# __slots__ is often used for optimize RAM