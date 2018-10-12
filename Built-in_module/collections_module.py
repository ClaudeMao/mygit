#collections模块提供了一些有用的集合类，可以根据需要选用。
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)