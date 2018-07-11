# !/usr/bin/python
# -*- coding: UTF-8 -*-
from concurrent.futures import ThreadPoolExecutor
import time
def sayhello(a):
    print("hello",a)
    time.sleep(2)
def main():
    print("this is main")
    while(True):
        with ThreadPoolExecutor(3) as executor:
            executor.submit(sayhello, '10')
        time.sleep(1)


if(__name__=='__main__'):
    main()
