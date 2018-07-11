# -*- coding: utf-8 -*-
import  codecs
from  sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
words =[
    "I come to China to travel",
    "This is a car polupar in China",
    "I love tea and Apple",
    "The work is to write some papers in science",
]
# print(vectorizer.fit_transform(words).toarray())
# print(vectorizer.get_feature_names())

for i  in range(1,100):
    print(i)