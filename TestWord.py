# -*- coding: utf-8 -*-
# import modules & set up logging
import logging
import os
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence('./in_the_name_of_people_segment.txt')

model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)
model.wv.get_vector()
req_count = 5
for key in model.wv.similar_by_word('沙瑞金', topn =100):
    if len(key[0])==3:
        req_count -= 1
        print (key[0], key[1])
        if req_count == 0:
            break;
print(model.wv.similarity('沙瑞金', '高育良'))
print(model.wv.similarity('李达康', '王大路'))
print(model.wv.doesnt_match(u"沙瑞金 高育良 李达康 刘庆祝".split()))


