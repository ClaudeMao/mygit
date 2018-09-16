class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print('name:{}, score:{}'.format(self.name,self.score))
    
    def dis_grade(self):
        if self.score >=90:
            print('A')
        elif self.score >=80:
            print('B')
        elif self.score >=70:
            print('C')
        elif self.score >= 60:
            print('D')
        else:
            print('sorry kid, you failed exam')

Ivy = Student('Ivy',86)
Ivy.print_score()
Ivy.dis_grade()		