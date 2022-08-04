#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/7/21 16:47
# @Author : LinYao
# @File : practice.py
'''
1. 已知一个字符串为 “hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
'''
test = "hello_world_yoyo"
print(test.split("_"))

'''
2. 有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”
'''
test=["hello", "world", "yoyo"]
print("_".join(test))

'''
3. 
'''