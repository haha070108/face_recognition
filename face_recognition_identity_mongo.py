# 识别图片中的人脸
import face_recognition
import time
from pyMongoConnUri import MyMongoDB
import  datetime
mongo = MyMongoDB()
data = mongo.dbfind(dic={})
list_faces = []
map_relation={}
i=0
for result in data:
    # map[result["name"]] =result["face_encoding"]
    map_relation[i]=result["name"]
    list_faces.append((result["face_encoding"]))
    i=i+1
unknown_image = face_recognition.load_image_file("lib1/20180709162730.jpg");
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
distance =face_recognition.face_distance(list_faces,unknown_encoding)
print(type(distance))
k =0
result_list= []
for val in list(distance):
    if(val<0.42):
        result_list.append((val,map_relation[k]))
    k=k+1
result_list.sort()
print(result_list[0][1])
for kk in result_list:
    print(kk)