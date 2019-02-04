import hello
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

print(hello.__name__)
print(__name__)