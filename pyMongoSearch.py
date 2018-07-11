#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import  face_recognition
import  os ,sys
import time

settings = {
    "ip":'192.168.109.136',   #ip
    "port":20000,           #端口
    "db_name" : "facedb",    #数据库名字
    "set_name" : "faceset" ,  #集合名字
    "username" : "root",
    "password":"xskj2017",
    "authSource":"admin"
}

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"],username=settings["username"], password =settings["password"],authSource=settings["authSource"])
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
        list=[]
        for result in data:
            #print(result["name"],result["face_encoding"])
            list.append(result["face_encoding"])

        jobs_image = face_recognition.load_image_file("lib/1521001573702701068.JPG");
        jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
        print("true pci",jobs_encoding)
        now_time = time.time()
        results = face_recognition.compare_faces(list, jobs_encoding, tolerance=0.3)
        end_time = time.time()
        print("spend time :", (end_time - now_time))
        for i in range(0, len(results)):
            if results[i] == True:
                print('The person is:',"1521001573702701068.JPG")

def main():

    mongo = MyMongoDB()
    # dic = {"name": "lisi","face_incoding": jobs_encoding.tolist()}
    # mongo.insert(dic)
    mongo.dbfind({})

if __name__ == "__main__":
    main()