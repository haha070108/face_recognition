#!/usr/bin/env python
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import os
import time
from  nearPyDev import MyMongoDB
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
from nearpy.distances import EuclideanDistance
import  logging
setting = {
    "path": "/root/python_app/upload/",
    "logging":"/root/python_app/logs/dirwatch.log"
}
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=setting['logging'],
                    filemode='w')
def endWith(s, *endstring):
    array = map(s.endswith, endstring)
    if True in array:
        return True
    else:
        return False


def watchFold(path, mongo, engine):
    s = os.listdir(path)
    for i in s:
        try:
            if endWith(i, '.png', '.img', '.jpg'):
                pic_path = path + i
                logging.info("process pic: "+ pic_path)
                query = mongo.get_source_pic_feature(pic_path)
                # if(query == None):
                #     continue
                # print(query)
                mongo.findKnnProcess(mongo, engine, query, i,pic_path)
                # //处理逻辑

        except Exception as es:
            logging.error(es)
        finally:
            os.remove(pic_path)


def main():
    logging.info("this is main")
    dimension = 128
    # Create a random binary hash with 10 bits
    rbp = RandomBinaryProjections('rbp', 10)

    # Create engine with pipeline configuration
    engine = Engine(dimension, lshashes=[rbp], distance=EuclideanDistance())

    mongo = MyMongoDB()
    # dic = {"name": "lisi","face_incoding": jobs_encoding.tolist()}
    # mongo.insert(dic)
    mongo.dbfind({}, engine)
    while (True):
        with ThreadPoolExecutor(1) as executor:
            executor.submit(watchFold(setting["path"], mongo, engine))
            executor.shutdown()
        time.sleep(1)
        logging.info("waiting.....")


if __name__ == "__main__":
    main()
