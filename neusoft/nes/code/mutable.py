#!/usr/bin/python
# -*- coding:UTF-8 -*-

#如 changeList(m)，则是将 m 真正的传过去，修改后changeList外部的m也会受影响。
def changeList(list):
    list += "7"
    print("函数内取值:", list)
    return

m = ["5", "6"]
changeList(m)
print("函数外取值:", m)