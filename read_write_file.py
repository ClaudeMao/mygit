try:
    f = open('U:/shefgit/mygit/readme.txt', 'r')#读取二进制文件用rb
    print(f.read()) # 文件过大一次性read的话会内存爆掉
finally:
    if f:
        f.close()
		#等价于 with open('U:/shefgit/mygit/readme.txt', 'r') as f:
		#           print(f.read())
		#可以省去调用f.close(),此方法优于上面

f = open('U:/shefgit/mygit/readme.txt', 'r') #写入用w,写入二进制用wb
for line in f.readlines():
	print(line.strip())
f.close()