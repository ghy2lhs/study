#!/usr/bin/python
# -*- coding: UTF-8 -*-

import zipfile

def extractFile(toPath,zFile,password):
    "不断调用zipfile模块的extractall方法尝试解压文件到toPath路径"
    try:
        zFile.extractall(path=toPath,pwd=password)
        print("SUCCESS-->"+password)
        return password
    except Exception:
        return

def main():
    zFile = zipfile.ZipFile("/Users/gonghaiyu/Desktop/neusoft/nes/code/test.zip")
    passFile = open("/Users/gonghaiyu/Desktop/neusoft/nes/code/passwords.txt")
    for line in passFile.readlines():
        password = line.strip('\n')
        guess =extractFile("/Users/gonghaiyu/Desktop/neusoft/nes/code",zFile,password)
        if guess:
            print("SUCCESS-->"+password)
            exit(0)


if __name__=='__main__':
    main()






