#!/usr/bin/python
# -*- coding:UTF-8 -*-

#定义可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n 
    return sum

#当可变参数调用组装的列表:
print(calc(*[1,2,3]))

#当可变参数调用已经存在的列表：
nums = [1,2,3]
print(calc(*nums))

#当可变参数调用组装的元组：
print(calc(*(1,3,5,7)))
print(calc(1,3,5,7))

#当可变参数调用已经存在的元组：
n = (1,3,5,7)
print(calc(*n))
#print(calc(n))会报错

