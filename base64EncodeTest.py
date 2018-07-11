#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  base64
import  os
import uuid
f=open(r'lib/b.jpg','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
print(ls_f)
print(str(ls_f,"utf-8"))
f.close()