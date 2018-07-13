import json
import nltk
from nltk import stem
import random
#from nltk.stem.wordnet import WordNetLemmatizer
import pickle
import ast

business_id_list = []

def filter_restaurants():
    global business_id_list
    with open('yelp_academic_dataset_business.json') as f:
        for line in f:
            business_info = json.loads(line)
            if "Restaurants" in business_info["categories"] and business_info['business_id'] not in business_id_list:
                business_id_list.append(business_info['business_id'])
    f.close()

def bigram_training():
    stemmer = stem.snowball.EnglishStemmer()

    restaurant_data = []
    fw2 = open("lineno",'w')
    fw = open("yelp_reviews_bigram",'w')
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_tot = 0
    i=0
    lineno_list = []
    with open('yelp_academic_dataset_review.json') as f:
        for line in f:
            business_review_info = json.loads(line)
            i=i+1
            if business_review_info['business_id'] in business_id_list and business_review_info["stars"]!='' and business_review_info["text"]!='' and count_tot <= 10000:
                if business_review_info["stars"] == 5 and count_5 <= 2000:
                    lineno_list.append(i)
                    count_5+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 4 and count_4 <= 2000:
                    lineno_list.append(i)
                    count_4+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 3 and count_3 <= 2000:
                    lineno_list.append(i)
                    count_3+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 2 and count_2 <= 2000:
                    lineno_list.append(i)
                    count_2+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 1 and count_1 <= 2000:
                    lineno_list.append(i)
                    count_1+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    fw2.write(str(i)+'\n')


    fw.close()
    f.close()
    fw2.close()


def extract_training():
    stemmer = stem.snowball.EnglishStemmer()

    restaurant_data = []
    fw2 = open("lineno",'w')
    fw = open("yelp_reviews",'w')
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_tot = 0
    i=0
    lineno_list = []
    with open('yelp_academic_dataset_review.json') as f:
        for line in f:
            business_review_info = json.loads(line)
            i=i+1
            if business_review_info['business_id'] in business_id_list and business_review_info["stars"]!='' and business_review_info["text"]!='' and count_tot <= 25000:
                if business_review_info["stars"] == 5 and count_5 <= 5000:
                    lineno_list.append(i)
                    count_5+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 4 and count_4 <= 5000:
                    lineno_list.append(i)
                    count_4+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 3 and count_3 <= 5000:
                    lineno_list.append(i)
                    count_3+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 2 and count_2 <= 5000:
                    lineno_list.append(i)
                    count_2+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    fw.write('\n')
                    fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 1 and count_1 <= 5000:
                    lineno_list.append(i)
                    count_1+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    fw.write('\n')
                    fw2.write(str(i)+'\n')


    fw.close()
    f.close()
    fw2.close()

def extract_test():
    global business_id_list
    stemmer = stem.snowball.EnglishStemmer()
    fr = open("lineno",'r')
    lines = fr.readlines()
    train_list = []
    for i in range(0,len(lines)):
        sublist = []
        sublist = eval(lines[i])
        train_list.append(sublist)
    fr.close()
    print(train_list)
    fw = open("yelp_test",'w')
    count_pos = 0
    count_neg = 0
    count_neut = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_tot = 0
    i=0
    lineno_list = []
    with open('yelp_academic_dataset_review.json') as f:
        for line in f:
            business_review_info = json.loads(line)
            i=i+1
            if business_review_info['business_id'] in business_id_list and business_review_info["stars"]!='' and business_review_info["text"]!='' and count_tot <= 10000 and i not in train_list:
                if business_review_info["stars"] == 5 and count_5 <= 2000:
                    lineno_list.append(i)
                    count_5+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    # for i in range(0,len(tokens)-1):
                    #     fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 4 and count_4 <= 2000:
                    lineno_list.append(i)
                    count_4+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    # for i in range(0,len(tokens)-1):
                    #     fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 3 and count_3 <= 2000:
                    lineno_list.append(i)
                    count_3+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    # for i in range(0,len(tokens)-1):
                    #     fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 2 and count_2 <= 2000:
                    lineno_list.append(i)
                    count_2+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    # for i in range(0,len(tokens)-1):
                    #     fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 1 and count_1 <= 2000:
                    lineno_list.append(i)
                    count_1+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]).encode('utf-8'))+' ')
                    # for i in range(0,len(tokens)-1):
                    #     fw.write(str(stemmer.stem(tokens[i]).encode('utf-8')+'|'+stemmer.stem(tokens[i+1]).encode('utf-8')+' '))
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')
            print("count",count_tot)

def shuffle():
    fr = open('yelp_reviews','r')
    fw = open('yelp_shuffled','w')
    lines = fr.readlines()
    random.shuffle(lines)
    for line in lines:
        fw.write(line)
    fw.close()
    fr.close()

def start():
    filter_restaurants()
    #extract_training()
    #shuffle()
    extract_test()
    #bigram_training()

start()
