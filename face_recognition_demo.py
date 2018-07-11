#!/usr/bin/env python
#-*- coding:utf-8 -*-
import  face_recognition
import  cv2
img = face_recognition.load_image_file("lib/20180613161929.jpg")
print(img)
face_locations = face_recognition.face_locations(img)
print (face_locations)
faceNum = len(face_locations)
print(faceNum)
img = cv2.imread("lib/20180613161929.jpg")
cv2.namedWindow("原图")
cv2.imshow("原图", img)
# 遍历每个人脸，并标注
for i in range(0, faceNum):
    top =  face_locations[i][0]
    right =  face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]

    start = (left, top)
    end = (right, bottom)

    color = (55,255,155)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)

# 显示识别结果
cv2.namedWindow("识别")
cv2.imshow("识别", img)

cv2.waitKey(0)
cv2.destroyAllWindows()