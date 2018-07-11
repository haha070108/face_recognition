import face_recognition
import  numpy
picture_of_me = face_recognition.load_image_file("lib/2008_001322.jpg")
my_face_encoding1 = face_recognition.face_encodings(picture_of_me)
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("lib/a2.jpg")

unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
# Now we can see the two face encodings are of the same person with `compare_faces`!

# dist = numpy.linalg.norm(my_face_encoding - unknown_face_encoding)
# print(dist)
rs= face_recognition.face_distance(my_face_encoding1,unknown_face_encoding)
print(rs)
results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
print(results)
print(type(results))
if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
list =[6.14,7.45,15.5]
def getScore(dist):
    score= 0
    if(dist < list[0] * 0.333):
        score = 1
    elif (dist < list[0]):
        score = (1.5*(list[0] - dist) / list[0] * 0.2 + 0.8);
    elif ((dist >= list[0]) and (dist <= list[1])):
        score =   (0.8 - (dist - list[0]) / ((list[1] - list[0])) * 0.2)
    elif ((dist > list[1]) and (dist < list[2])):
        score =   ((list[2] - dist) / (list[2] - list[1]) * 0.6)
    elif (dist > list[2]):
       score = 0
    return score

print("rs",getScore(rs[0]))
print("rs",getScore(rs[1]))
print("rs",getScore(rs[2]))