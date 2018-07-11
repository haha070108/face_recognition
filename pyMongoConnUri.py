#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import  face_recognition
import  os ,sys

settings = {
    "ip":'10.10.1.18',   #ip
    "port":27017,           #端口
    "db_name" : "facedb",    #数据库名字
    "set_name" : "faceset" ,  #集合名字
    "username" : "root",
    "password":"xskj2017",
    "authSource":"admin"

}

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self,dic):
        print("inser...")
        self.my_set.insert(dic)

    def update(self,dic,newdic):
        print("update...")
        self.my_set.update(dic,newdic)

    def delete(self,dic):
        print("delete...")
        self.my_set.remove(dic)

    def dbfind(self,dic):
        print("find...")
        data = self.my_set.find(dic)
        return data

def main():

    mongo = MyMongoDB()
    # dic = {"name": "lisi","face_incoding": jobs_encoding.tolist()}
    # mongo.insert(dic)
    # mongo.dbfind({"name":"zhangsan"})
    #
    # mongo.update({"name":"zhangsan"},{"$set":{"age":"25"}})
    # mongo.dbfind({"name":"zhangsan"})
    #
    # mongo.delete({"name":"zhangsan"})
    # mongo.dbfind({"name":"zhangsan"})
    path ="F:\\sss\\"
    dirs  =os.listdir(path)
    count =0;
    for file in dirs:
        insert_pic = face_recognition.load_image_file(path+file)
        print(path+file)

        pic_encoding = face_recognition.face_encodings(insert_pic)
        if (len(pic_encoding)>0):
          dic = {"name": file, "face_encoding": pic_encoding[0].tolist(),"status":0}
          mongo.insert(dic)
        else:
            continue
        count=count +1
        print(count)

if __name__ == "__main__":
    main()