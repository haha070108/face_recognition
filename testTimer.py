#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
def fun_timer():
    print('hello timer')   #打印输出
    timer = threading.Timer(2,fun_timer)   #60秒调用一次函数
    # 定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
    timer.start()  # 启用定时器
fun_timer()