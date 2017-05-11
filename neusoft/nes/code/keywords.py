#!/usr/bin/python
# -*-coding:UTF-8 -*-

def person(name,age=30,**kw):
    print("name:",name,"age:",age,"other:",kw)

person('Michael',20)
person('Bob',35,city='Beijing')
person('Adam', 45, gender='M', job='Engineer')