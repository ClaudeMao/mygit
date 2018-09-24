class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path): #若无attr，则加入一个
        return Chain('%s/%s' % (self._path, path))

    def __str__(self): #用于调用Chain()时直接显示字符
        return self._path

    __repr__ = __str__ #用于调用Chain()时直接显示字符
    
print(Chain().status.user.timeline.list)