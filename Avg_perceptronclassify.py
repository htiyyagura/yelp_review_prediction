__author__ = 'maheshkumarlunawat'

import sys
import json

file_model_path = sys.argv[1]
file_test_path = sys.argv[2]

file_model = open(file_model_path)
dict_main = json.load(file_model)
file_model.close()

dict_labels = dict_main['$@labels@$']
total_labels = dict_labels['$@total-labels-total@$']
file_test = open(file_test_path)
for line in file_test:
    weightMax = -12345678
    labelMaxNum = -1
    for i in range (1, total_labels+1):
        weightCurr = 0
        dict_type = dict_main[str(i)]
        words=line.split(' ')
        for j in range(1,len(words)):
            if words[j] in dict_type:
                weightCurr+=dict_type[words[j]]
        if weightMax < weightCurr:
            weightMax = weightCurr
            labelMaxNum = i
    labelResult = dict_labels[str(labelMaxNum)]
    # if (str(labelResult)=='1' or str(labelResult)=='2'):
    #     print('negative')
    # elif (str(labelResult)=='4' or str(labelResult)=='5'):
    #     print('positive')
    # else:
    #     print('neutral')
    print(labelResult)
file_test.close()



