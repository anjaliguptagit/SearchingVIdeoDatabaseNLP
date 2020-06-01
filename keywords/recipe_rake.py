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
words=[]
n=len(topics['Description'])
for i in range(0,n):
    #text= re.sub('[^a-zA-Z]', ' ', recipes['title'][i])
    #text= text.lower()
    #text= text.split(' ')
    #text=list(filter(lambda x:x!='',text))
    text=rake.funrake(topics['Description'][i]);
    words.append(text)
#print(words)
def search(sentence):
    sentence= re.sub('[^a-zA-Z]', ' ',sentence)
    sentence= sentence.lower()
    sentence= sentence.split(' ')
    sentence= list(filter(lambda x:x!='',sentence))
    rank=[]
    for i in words:
        n=0;
        for j in sentence:
            if j in i:
                n=n+1
        rank.append(n)
    topic1=topics.assign(number_rank=rank)
    #print(recipe1)
    topic1=topic1.sort_values(by='number_rank',ascending=False)
    return topic1
import cv2
import time

#listing the sorted titles of video
print(search('evastating green house book shoppping// study')['Title'][0:7])

#taking input from user to select a video
n=int(input("your choice"))
link=search('evastating green house book shoppping// study')['link'][n]

#print(link)

#Play the video, press q to stop playing the video
vs = cv2.VideoCapture(link)
time.sleep(2.0)
while True:
    frame = vs.read()
    frame = frame[1]
    frame = imutils.resize(frame, width=600)
    if frame is None:
       break
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()
