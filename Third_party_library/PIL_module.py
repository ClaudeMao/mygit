from PIL import Image

im = Image.open('C:/Users/98415/Desktop/death.jpg')
w,h = im.size
print('Original image size:{}*{}'.format(w,h))
# im.show()
im.thumbnail((w//2, h//2))
print('Resize image to:{}*{}'.format(w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')