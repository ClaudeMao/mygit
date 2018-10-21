from PIL import Image

im = Image.open('death.jpg')
w,h = im.size
print('Original image size:{}*{}'.format(w,h))