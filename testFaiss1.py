#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  numpy as np
import swigfaiss as faiss
import face_recognition
from pyMongoConnUri import MyMongoDB
mongo = MyMongoDB()
data = mongo.dbfind(dic={})
list_faces = []
for result in data:
    # map[result["name"]] =result["face_encoding"]
    list_faces.append((result["face_encoding"]))
unknown_image = face_recognition.load_image_file("lib/20180709162714.jpg");
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
ss =np.asarray(list_faces).astype('float32')
unknow_pic=np.asarray([unknown_encoding]).astype('float32')
print(np.shape(ss))
d =128                           # dimension
nlist = 100
quantizer = faiss.IndexFlatL2(d)  # the other index
index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)
index.train(ss)
index.add(ss)                  # add vectors to the index
print(index.ntotal)
k = 5                          # we want to see 4 nearest neighbors
D, I = index.search(unknow_pic, k)     # actual search
print(I)                   # neighbors of the 5 first queries
print(D)
