class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count +=1 
    def print_name(self):
        print(self.name)
ivy = Student('Ivy')
ivy.print_name()
print(Student.count)
claude = Student('Claude')
claude.print_name()
print(Student.count)