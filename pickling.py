'''
import pickle #pickle只适用于python
d = dict(name = 'Claude', age = 22, score = 99)
f = pickle.dumps(d) #用pickle.dumps()将变量序列化
print(f)
g = pickle.loads(f) #用pickle.loads()反序列化
print(g)
'''

import json #json适用广，是一种标准格式，比XML快
d = dict(name = 'Claude', age = 22, score = 99)
f = json.dumps(d)
print(f)
g = json.loads(f) 
print(g)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
        }
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default = lambda obj: obj.__dict__))
# 此方法对定义了__slots__的无效， 因为无__dict__属性

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook = dict2student))
#object_hook用来把dict转换为Student实例
def dict3(h):
    return dict(name = h['name'], age = h['age'])

obj = dict(name= '小明', age=20)
print(json.dumps(obj, ensure_ascii = True))#ensure_ascii True是将中文转换成二进制编码
s = json.dumps(obj, ensure_ascii=True)
print(json.loads(s, object_hook = dict3))
#json.dumps变为str后，用loads里的object_hook的函数再转回dict