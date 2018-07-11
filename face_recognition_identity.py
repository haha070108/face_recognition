# 识别图片中的人脸
import face_recognition
import time
import  datetime
import  numpy as np
jobs_image = face_recognition.load_image_file("lib/000179_02159509.jpg");
unknown_image = face_recognition.load_image_file("lib/000190_02159501.jpg");
now_time = time.time()
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
ss =np.asarray([jobs_encoding,jobs_encoding])
print(np.shape(ss))
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
print(type(unknown_encoding))
distance =face_recognition.face_distance([jobs_encoding],unknown_encoding)
print(distance)
results = face_recognition.compare_faces([jobs_encoding], unknown_encoding ,tolerance=0.4)
labels = ['a1', 'b1']
print('results:',(results))
# print(type(results))
for i in range(0, len(results)):
    if results[i] == True:
        print('The person is:'+labels[i])
end_time = time.time()