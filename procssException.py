#!/usr/bin/env python
#-*- coding:utf-8 -*-
def showMessage():
    try:
        a=100
        b=0
        a/b
    except Exception as es:
        print(es)
    else:
        print("process is ok....")
    finally:
        print("release resources ....")

def main():
    showMessage()
if __name__=="__main__":
    main()