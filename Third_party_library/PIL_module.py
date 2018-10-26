from PIL import Image
import os
print(os.getcwd())
os.chdir('C:/Users/98415/Desktop') # 修改工作目录
print(os.getcwd())

file = '310px-Beta_Negative_Decay.png'
im = Image.open(file)
# im.rotate(45).show() # 旋转45度
w,h = im.size
print('Original image size:{}*{}'.format(w,h))
# im.show() 显示图片

im.thumbnail((w//2,h//2))
print('Resize image to:{}*{}'.format(w//2, h//2))
im.save('thumbnail.png', 'png')