import face_recognition

image = face_recognition.load_image_file("lib/2008_001322.jpg")
faces =face_recognition.face_encodings(image)
print(len(faces))
print(faces)
face_landmarks_list = face_recognition.face_landmarks(image)
print(type(face_landmarks_list))
for i in  range(0,len(face_landmarks_list)):
    print(face_landmarks_list[i])

# face_landmarks_list is now an array with the locations of each facial feature in each face.
# face_landmarks_list[0]['left_eye'] would be the location and outline of the first person's left eye.
