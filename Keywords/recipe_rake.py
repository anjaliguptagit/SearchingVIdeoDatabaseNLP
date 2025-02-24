import cv2
import sys
import time
import pandas as pd
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

topics=pd.read_csv("/media/anjali/0EFF08340EFF0834/SpeechRecog_ubuntu/Keywords/Vid.csv")
words = []
n=len(topics['Description'])

for i in range(0,n):
	text = rake.funrake(topics['Description'][i]);
	words.append(text)

def search(sentence):
	sentence = re.sub('[^a-zA-Z]', ' ',sentence)
	sentence = sentence.lower()
	sentence = sentence.split(' ')
	sentence = list(filter(lambda x:x!='',sentence))
	phrases = []
	phrase = " " 
	stopwords_plus=['the','is','this','that','which','where','when','how','what']
	for word in sentence:
		if word not in stopwords_plus:
			if phrase==" ":
				phrase=word
				phrase+=" "
			else:
				phrase+=word
				phrase+=" "
		elif word in stopwords_plus:
			if phrase!=" ":
				phrases.append(phrase)
				phrase=" "
	phrases.append(phrase)
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

#input_keyword = input("Enter the query\n")
input_keyword = ''
for i in range(1, len(sys.argv)):
	input_keyword += (sys.argv[i] + ' ')
title_list = list(search(input_keyword)['Title'][0:5])

file1 = open("result.txt","w")
  
# \n is placed to indicate EOL (End of Line) 
for line in title_list:
	line = (line[11:-4])
	file1.write(line+".mp4"+"\n") 

file1.close()

