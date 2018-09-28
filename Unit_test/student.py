class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if 60 <= self.score <= 79:
            return 'B'
        elif 80 <= self.score <= 100: #用elif 而不是else if
            return 'A'
        elif 0 <= self.score <= 59:
            return 'C'
        else:
            raise ValueError('wrong entering')
			