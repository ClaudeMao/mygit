from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1
    
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
print(bart)