from __future__ import division
from collections import defaultdict
import numpy as np 
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import cv2

def funrake(Text):
    text= re.sub('[^a-zA-Z]', ' ', Text)
    text= text.lower()
    text= text.split(' ')
    text=list(filter(lambda x:x!='',text))
    POS_tag = nltk.pos_tag(text)
    from nltk.stem import WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    adjective_tags = ['JJ','JJR','JJS']
    lemmatized_text = []
    for word in POS_tag:
        if word[1] in adjective_tags:
            lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
        else:
            lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0])))
    #time to get rid of stopwords
    stopwords = []
    wanted_POS = ['NN','NNS','NNP','NNPS','JJ','JJR','JJS','VBG','FW'] 
    for word in POS_tag:
        if word[1] not in wanted_POS:
            stopwords.append(word[0])
    stopword_file = open("/media/anjali/0EFF08340EFF0834/SpeechRecog_ubuntu/Keywords/stopwords.txt", "r")
    lots_of_stopwords = []
    for line in stopword_file.readlines():
        lots_of_stopwords.append(str(line.strip()))
    stopwords_plus = []
    stopwords_plus = stopwords + lots_of_stopwords
    stopwords_plus = set(stopwords_plus)
    
    phrases = []
    phrase = " "
    for word in lemmatized_text:
        
        if word in stopwords_plus:
            if phrase!= " ":
                phrases.append(str(phrase).split())
            phrase = " "
        elif word not in stopwords_plus:
            phrase+=str(word)
            phrase+=" "
    frequency = defaultdict(int)
    degree = defaultdict(int)
    word_score = defaultdict(float)
    
    vocabulary = []
    
    for phrase in phrases:
        for word in phrase:
            frequency[word]+=1
            degree[word]+=len(phrase)
            if word not in vocabulary:
                vocabulary.append(word)
                
    for word in vocabulary:
        word_score[word] = degree[word]/frequency[word]
    phrase_scores = []
    keywords = []
    phrase_vocabulary=[]
    
    for phrase in phrases:
        if phrase not in phrase_vocabulary:
            phrase_score=0
            for word in phrase:
                phrase_score+= word_score[word]
            phrase_scores.append(phrase_score)
            phrase_vocabulary.append(phrase)
    
    phrase_vocabulary = []
    j=0
    for phrase in phrases:
        
        if phrase not in phrase_vocabulary:
            keyword=''
            for word in phrase:
                keyword += str(word)+" "
            phrase_vocabulary.append(phrase)
            keyword = keyword.strip()
            keywords.append(keyword)
            j+=1
    sorted_index = np.flip(np.argsort(phrase_scores),0)
    sorted=[]
    for i in range(0,len(sorted_index)):
        #print(str(keywords[sorted_index[i]])+", ",)
        sorted.append(str(keywords[sorted_index[i]]))
    return sorted



