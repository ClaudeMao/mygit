class Screen(object):
    pass
    
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self, value):
        self._height = value
        
    @property
    def resolution(self):
        return self._width * self._height
        
s = Screen()
s.width = 1024
s.height = 768
print('resolution = {}'.format(s.resolution))