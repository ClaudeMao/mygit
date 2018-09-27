'''
import pdb

s = '0'
n = int(s)
pdb.set_trace() #运行到这里会暂停
print(10 / n)
'''

import logging
logging.basicConfig(level=logging.INFO)
#设置记录信息级别，输出信息

s = '0'
n = int(s)
logging.info('n = {}'.format(n))
print(10 / n)