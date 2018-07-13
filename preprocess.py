import json
import random

import nltk
from nltk import stem
vocab_dict = {}


business_id_list = []

def filter_restaurants():
    global business_id_list
    with open('yelp_academic_dataset_business.json') as f:
        for line in f:
            business_info = json.loads(line)
            if "Restaurants" in business_info["categories"] and business_info['business_id'] not in business_id_list:
                business_id_list.append(business_info['business_id'])
    f.close()


def extract_training():
    stemmer = stem.snowball.EnglishStemmer()

    restaurant_data = []
    #fw2 = open("lineno",'w')
    fw = open("yelp_reviews_25k",'w')
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
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    #fw.write('\n')
                    #fw2.write(str(i)+'\n')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]))+'|'+str(stemmer.stem(tokens[i+1]))+' ')
                    fw.write('\n')

                if business_review_info["stars"] == 4 and count_4 <= 5000:
                    lineno_list.append(i)
                    count_4+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    #fw.write('\n')
                    #fw2.write(str(i)+'\n')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]))+'|'+str(stemmer.stem(tokens[i+1]))+' ')
                    fw.write('\n')

                if business_review_info["stars"] == 3 and count_3 <= 5000:
                    lineno_list.append(i)
                    count_3+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    #fw.write('\n')
                    #fw2.write(str(i)+'\n')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]))+'|'+str(stemmer.stem(tokens[i+1]))+' ')
                    fw.write('\n')

                if business_review_info["stars"] == 2 and count_2 <= 5000:
                    lineno_list.append(i)
                    count_2+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    #fw.write('\n')
                    #fw2.write(str(i)+'\n')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]))+'|'+str(stemmer.stem(tokens[i+1]))+' ')
                    fw.write('\n')

                if business_review_info["stars"] == 1 and count_1 <= 5000:
                    lineno_list.append(i)
                    count_1+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    #fw.write('\n')
                    #fw2.write(str(i)+'\n')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]))+'|'+str(stemmer.stem(tokens[i+1]))+' ')
                    fw.write('\n')


    print(count_1,count_2,count_3,count_4,count_5,count_tot)
    fw.close()
    f.close()
    #fw2.close()

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
    fw = open("yelp_reviews_test",'w')
    count_pos = 0
    count_neg = 0
    count_neut = 0
    count_tot = 0
    i=0
    lineno_list = []
    with open('yelp_academic_dataset_review.json') as f:
        for line in f:
            business_review_info = json.loads(line)
            i=i+1
            if business_review_info['business_id'] in business_id_list and business_review_info["stars"]!='' and business_review_info["text"]!='' and count_tot <= 5000 and i not in train_list:
                if business_review_info["stars"] == 5 and count_pos <= 1000:
                    lineno_list.append(i)
                    count_pos+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')

                    #fw2.write(str(i)+'\n')
                    for i in range(0,len(tokens)-1):
                        fw.write(str(stemmer.stem(tokens[i]))+'|'+str(stemmer.stem(tokens[i+1]))+' ')
                    fw.write('\n')

                if business_review_info["stars"] == 4 and count_neg <= 1000:
                    lineno_list.append(i)
                    count_pos+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 3 and count_neut <= 1000:
                    lineno_list.append(i)
                    count_pos+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 2 and count_neut <= 1000:
                    lineno_list.append(i)
                    count_pos+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')

                if business_review_info["stars"] == 1 and count_neut <= 1000:
                    lineno_list.append(i)
                    count_pos+=1
                    count_tot+=1
                    tokens = nltk.word_tokenize(business_review_info["text"])
                    fw.write(str(business_review_info["stars"])+' ')
                    for i in range(0,len(tokens)):
                        fw.write(str(stemmer.stem(tokens[i]))+' ')
                    fw.write('\n')
                    #fw2.write(str(i)+'\n')


def shuffle():
    fr = open('yelp_reviews_25k','r')
    fw = open('yelp_shuffled_25k','w')
    lines = fr.readlines()
    random.shuffle(lines)
    for line in lines:
        fw.write(line)
    fw.close()
    fr.close()

def vocab_count():
    train_data = []
    global vocab_dict
    c = 0
    fr = open('yelp_shuffled_25k','r')
    #fw = open('vocab_dict','w')
    lines = fr.readlines()
    for i in range(0,len(lines)):
        #train_data.append(lines[i].split())
        line = lines[i].split()
        for i in range(1,len(line)):
            if line[i] not in vocab_dict:
                c=c+1
                vocab_dict[str(line[i])] = c

    fr.close()
    # for k,v in vocab_dict.items():
    #     print(k,v)

def extract_features():
    global vocab_dict
    fr = open('yelp_shuffled','r')
    fw = open('training_svm_yelp','w')
    lines = fr.readlines()
    for i in range(0,len(lines)):
        line = lines[i].split()
        fw.write(line[0]+' ')
        dict_line = {}
        for i in range(1,len(line)):
            if vocab_dict[line[i]] not in dict_line:
                dict_line[str(vocab_dict[line[i]])] = 1
            else:
                dict_line[str(vocab_dict[line[i]])]+= 1

        l = list(dict_line.keys())
        for i in range(0,len(l)):
            l[i] = int(l[i])
        l.sort()
        #print(l)

        for i in range(0,len(l)):
            fw.write(str(l[i])+':'+ str(dict_line[str(l[i])])+' ')
        fw.write('\n')
    fw.close()



def split_data():
    fr = open('training_svm_yelp','r')
    fw1 = open('train75_bi','w')
    fw2 = open('test25_bi','w')

    lines = fr.readlines()
    random.shuffle(lines)

    train =[]
    dev = []
    train = lines[:9375]
    dev = lines[9375:]

    for line in train:
        fw1.write(line)
    fw1.close()

    for line in dev:
        fw2.write(line)
    fw2.close()


def start():
    filter_restaurants()
    extract_training()
    shuffle()
    #extract_test()
    vocab_count()
    extract_features()
    split_data()

start()
