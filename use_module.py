#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 假装这是个模块 '

__author__ = 'Claude Mao'

import sys

def pretend():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, {}!'.format(args[1]))
    else:
        print('guna!')

if __name__=='__main__':
    pretend()

#直接执行.py时执行test，引用为模块时不执行test