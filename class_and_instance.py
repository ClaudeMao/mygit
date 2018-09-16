class Student(object):
    def __init__(self, name, score):
        self.__name = name  #前面加__表示私有变量，无法从外部访问(实际可以通过_Student__name访问)
        self.__score = score
        
    def print_score(self):
        print('name:{}, score:{}'.format(self.__name,self.__score))
    
    def dis_grade(self):
        if self.__score >=90:
            print('Grade:A')
        elif self.__score >=80:
            print('Grade:B')
        elif self.__score >=70:
            print('Grade:C')
        elif self.__score >= 60:
            print('Grade:D')
        else:
            print('sorry kid, you failed exam')

    def get_name(self):
        return self.__name
        
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('error')
        
Ivy = Student('Ivy', 86)
Ivy.print_score()
Ivy.dis_grade()
Ivy.set_score(950)