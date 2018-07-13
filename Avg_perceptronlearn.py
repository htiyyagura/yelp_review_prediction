from __future__ import division

import sys
import json
import math
import random


def totalDocs(file_training_path):
    f_training = open(file_training_path)
    total_docs = 0
    for line in f_training:
        total_docs+=1
    return total_docs

def updateAvgWeight():
    for i in range (1, total_labels+1):
        dict_type = dict_labels_value[i]
        dict_type_avg = dict_labels_value_avg[i]
        for key in dict_type:
            if key in dict_type_avg:
                dict_type_avg[key] += dict_type[key]
            else:
                dict_type_avg[key] = dict_type[key]
    return

def updateWeight(dict_type, line, value):
    for word in line.split(' ', 1)[1].split():
        if word in dict_type:
            dict_type[word]+=value
        else:
            dict_type[word]=value
    return


def calcerrorrate():
    global countLoop,total_labels,errorCurr,errorPrev
    line = file_training.seek(0)
    lines = file_training.readlines()
    random.shuffle(lines)
    errorCount = 0
    errorPrev=errorCurr
    for eachline in lines:
        line=eachline.strip()
        currLabel = line.split(' ', 1)[0]
        if currLabel not in dict_labels:
            total_labels+=1
            dict_labels[currLabel]=total_labels
            dict_labels_value[total_labels] = {}
            dict_labels_value_avg[total_labels] = {}

        currLabelNum=dict_labels[currLabel]
        weightMax = -12345678
        labelMaxNum = -1
        for i in range (1, total_labels+1):
            weightCurr = 0
            dict_type = dict_labels_value[i]
            for word in line.split(' ', 1)[1].split():
                if word in dict_type:
                    weightCurr+=dict_type[word]
            if weightMax < weightCurr:
                weightMax = weightCurr
                labelMaxNum = i

        if labelMaxNum != currLabelNum:
            #print("mismatch")
            updateWeight(dict_labels_value[labelMaxNum], line, -1)
            updateWeight(dict_labels_value[currLabelNum], line, 1)
            errorCount+=1
        #updateWeightAvg()
    updateAvgWeight()
    errorCurr=errorCount/total_docs
    #print(dict_labels_value)
    #print(dict_labels_value_avg)
    print('Loop number {} error rate {}'.format(countLoop, errorCount/total_docs))
    countLoop+=1

file_training_path = sys.argv[1]
file_model_path = sys.argv[2]

file_training = open(file_training_path)
total_docs = totalDocs(file_training_path)
print(total_docs)
total_labels = 0
dict_labels = {}
dict_vocab = {}
dict_labels_value = {}
dict_labels_value_avg = {}
countLoop = 1
errorPrev=0.001
errorCurr=0.0
# calcerrorrate()
# while abs(errorPrev-errorCurr) >= 0.001:
#     calcerrorrate()
while countLoop!=30:
    calcerrorrate()
file_training.close()

dict_labels_inverse ={}
for key in dict_labels:
    value=dict_labels[key]
    dict_labels_inverse[value]=key
dict_labels_inverse['$@total-labels-total@$']=total_labels
dict_labels_value_avg['$@labels@$']=dict_labels_inverse

file_model = open(file_model_path,'w')
json.dump(dict_labels_value_avg,file_model)
file_model.close()