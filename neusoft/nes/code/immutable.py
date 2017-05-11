#!/usr/bin/python
# -*- coding:utf-8 -*-

# 如ChangeInt（i1），传递的只是i1的值，没有影响i1对象本身。
# 比如在 ChangeInt（i）内部修改 i 的值，只是修改另一个复制的对象，不会影响 i 本身。
def ChangeInt(i):
    i = i+2
    print("内部i:"+str(i))

i1 = 73 
ChangeInt(i1)
print("外部i:"+str(i1))

