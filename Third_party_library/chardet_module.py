import chardet
print(chardet.detect(b'hello'))

data = '一二三四五'.encode('utf-8')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

