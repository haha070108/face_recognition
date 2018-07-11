# !/usr/bin/python
# -*- coding: UTF-8 -*-
# a =100
# a1=str(a)
# print(a+a1)
str ="/rot/asdfas/adfa/asdfaf.jpg"
arr =str.split("/")
print(len(arr))
print(arr[len(arr)-1])

def show_parass(a,b,*c ,**d):
    print(a)
    print(b)
    print(len(c))
    print("=================")
    for  i in c:
        print(i)
    print("===================")
    for key in d:
        print(key,"",d[key])
show_parass(1, 2, 3, 4, username="zhangsan", password="123456")