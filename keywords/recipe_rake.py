# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:09:51 2020

@author: Shwetha
"""
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:08:07 2020

@author: Shwetha
"""
import cv2
import time
import pandas as pd
topics=pd.read_csv("Vid.csv")
#print(recipes)
#recipes.columns
import numpy as np 
import re
import nltk
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import imutils
import rake
words = []

n=len(topics['Description'])

for i in range(0,n):
    text = rake.funrake(topics['Description'][i]);
    words.append(text)

#print(words)
def search(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ',sentence)
    sentence = sentence.lower()
    sentence = sentence.split(' ')
    sentence = list(filter(lambda x:x!='',sentence))
    rank=[]
    for i in words:
        n=0;
        for j in sentence:
            if j in i:
                n=n+1
        rank.append(n)
    topic1 = topics.assign(number_rank=rank)
    topic1 = topic1.sort_values(by='number_rank',ascending=False)
    return topic1

input_keyword = input("Enter the query\n")
title_list = list(search(input_keyword)['Title'][0:5])

#listing the sorted titles of video
print(f'{"          Title":70}', "      Time\n")

for title in title_list:
	name = title.split("/")[1]
	duration = int((title.split("/")[2]).split(".")[0])
	start_time = duration*5
	print(f'{name:70}', start_time,"-", start_time+5, "mins\n")



