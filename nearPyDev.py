#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy
import time
import face_recognition
from pymongo import MongoClient
import uuid
import os
import base64
from concurrent.futures import ThreadPoolExecutor
import logging
settings = {
    "ip": '10.10.1.18',  # ip
    "port": 27017,  # 端口
    "db_name": "facedb",  # 数据库名字
    "set_name": "faceset",  # 集合名字s
    "username": "root",
    "password": "xskj2017",
    "authSource": "admin",
    "threshold": 0.5,
    # 最终结果数据表
    "result_set": "face_recongnition_result",
    # 原始图片表空间
    "read_init": "facesetInit",
    "tmp_pic_path": "/root/python_app/tmp_pics/",
    "logging":"/root/python_app/logs/nearPyDev.log"
}

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=settings['logging'],
                    filemode='w')


class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            logging.info(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]
        self.result_set = self.db[settings["result_set"]]
        self.read_init = self.db[settings["read_init"]]
    def dbfindAllFeatures(self,dict):
       # print("find...")
        data = self.my_set.find(dict)
        return data
    def insert(self, dic):
        logging.info("inser...")
        self.result_set.insert(dic)

    def update(self, dic, newdic):
        logging.info("update...")
        self.read_init.update(dic, newdic)

    def delete(self, dic):
        logging.info("delete...")
        self.my_set.remove(dic)

    def process_pic(self, dic):

        logging.info("process pic start....")
        data = self.read_init.find(dic)
        for result in data:
            try:
                start_time = time.time()
                id = result["id"]
                img_encoding = result["img_path"]
                logging.info("id: "+ id)
                # 解码数据
                pic = settings["tmp_pic_path"] + uuid.uuid4().hex + ".jpg";
                new_file = open(pic, "xb")
                img_data = base64.b64decode(img_encoding)
                new_file.write(img_data)
                new_file.close()
                insert_pic = face_recognition.load_image_file(pic)
                pic_encoding = face_recognition.face_encodings(insert_pic)
                if (len(pic_encoding) > 0):
                    dic = {"name": id, "face_encoding": pic_encoding[0].tolist()}
                    self.my_set.insert(dic)
                os.remove(pic)
                # 更新原始表的数据
                update_dic = {"id": id}
                new_dic = {"$set": {"status": 1}}
                self.update(update_dic, new_dic)
                now_time = time.time()
                print("spend time :" + str(now_time - start_time))
            except Exception as es:
                logging.error(es)
            else:
                logging.info("process is ok")
            finally:
                logging.info("process  source img is over....")


    def dbfind(self, dic, engine):

        logging.info("find...")
        data = self.my_set.find(dic)
        for result in data:
            # print(result["name"],result["face_encoding"])
            engine.store_vector(numpy.asarray(result["face_encoding"]), result["name"])
        logging.info("load data into memeory is ok.....")

    def findKnn(self, engine, query):
        start_time = time.time()
        N = engine.neighbours(query)
        now_time = time.time()
        logging.info(N)
        logging.info("search mongo pic:"+ N[0][1])
        logging.info("search mongo sim:"+ str(N[0][2]))
        if (N[0][2] < settings["threshold"]):
            logging.info("find one")
            logging.info("spend time :%f" +str(now_time - start_time))

    def findKnnProcess(self, mongo, engine, query, img,pic_path):
        start_time = time.time()
        N = engine.neighbours(query)
        print(N)
        now_time = time.time()
        with open(pic_path, 'rb') as f:
            ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        if (len(N) > 0):
            print("search mongo pic:"+ N[0][1])
            print("search mongo sim:"+str(N[0][2]))
            if (N[0][2] < settings["threshold"]):
                logging.info("find one")
                position = img.index(".jpg")
                uuid = img[0:position]
                dic = {"id": uuid, "id_card": N[0][1],"timestamp":now_time,"img":ls_f.decode()}
                # save to mongodb for process
                mongo.insert(dic)
                logging.info("spend time :" +str(now_time - start_time))
    def findKnnProcessNewWithFaiss(self, mongo, query, img,pic_path,index,map_relation):
        start_time = time.time()
        with open(pic_path, 'rb') as f:
            ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        np_search_pic = numpy.asarray([query]).astype('float32')
        k = 5  # we want to see 5 nearest neighbors
        D, I = index.search(np_search_pic, k)  # actual search
        logging.info(D)
        logging.info(I)
        similarities="" #欧式距离值
        idcards=""#结果ID
        for j in I[0]:
            idcards = idcards + map_relation[int(j)] +" "
        logging.info(idcards)
        for i in D[0]:
            similarities = similarities + str(pow(i, 0.5)) +" "
        logging.info(similarities)
        now_time = time.time()
        if(len(I[0])>0):
            id_card = map_relation[int(I[0][0])]
            position = img.index(".jpg")
            uuid = img[0:position]
            logging.info("find one")
            dic = {"id": uuid, "id_card": id_card, "timestamp": now_time, "img": ls_f.decode()}
            # save to mongodb for process
            if(D[0][0]<settings["threshold"]):
              mongo.insert(dic)
        logging.info("spend time :" + str(now_time - start_time))

    def findKnnProcessNew(self, mongo, query, img,pic_path,list_faces,map_relation):
        start_time = time.time()
        with open(pic_path, 'rb') as f:
            ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        distance = face_recognition.face_distance(list_faces, query)
        k = 0
        result_list = []
        for val in list(distance):
            if (val < settings["threshold"]):
                result_list.append((val, map_relation[k]))
            k = k + 1
        now_time = time.time()
        if(len(result_list)>0):
            result_list.sort()
            print(result_list)
            position = img.index(".jpg")
            uuid = img[0:position]
            logging.info("find one")
            dic = {"id": uuid, "id_card": result_list[0][1], "timestamp": now_time, "img": ls_f.decode()}
            # save to mongodb for process
            mongo.insert(dic)
        logging.info("spend time :" + str(now_time - start_time))

    def get_source_pic_feature(self, pic_path):
        # "lib/20180613093931.jpg"
        jobs_image = face_recognition.load_image_file(pic_path);
        jobs_encoding= face_recognition.face_encodings(jobs_image)
        if(len(jobs_encoding)>0):
            query = numpy.asarray(jobs_encoding[0])
            return query


def main():
    # dimension = 128
    # rbp = RandomBinaryProjections('rbp', 10)
    # engine = Engine(dimension, lshashes=[rbp],distance=EuclideanDistance())
    mongo = MyMongoDB()
    # mongo.dbfind({},engine)
    # print("search pic: ","20180613093931.jpg")
    # query = mongo.get_source_pic_feature("lib/a.jpg")
    # mongo.findKnn(engine,query)
    while (True):
        with ThreadPoolExecutor(1) as executor:
            dic = {"status": 0}
            executor.submit(mongo.process_pic(dic))
            executor.shutdown()
        time.sleep(1)
        logging.info("waiting.....")


if __name__ == "__main__":
    main()
