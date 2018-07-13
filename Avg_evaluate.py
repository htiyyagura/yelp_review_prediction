from __future__ import division
import sys


def accuracyPos():
    for line in trainFIle:
        words=line.split(' ')
        if (str(words[0])=='1' or str(words[0])=='2'):
            labels.append('negative')
        elif (str(words[0])=='4' or str(words[0])=='5'):
            labels.append('positive')
        else:
            labels.append('neutral')

testFile=open("label.txt")
trainFIle=open("yelp_test")
labels=[]
correct=0
one=0
two=0
three=0
four=0
five=0
classified_one=0
classified_two=0
classified_three=0
classified_four=0
classified_five=0
correct_one=0
correct_two=0
correct_three=0
correct_four=0
correct_five=0

testline=testFile.readlines()
total=len(testline)
print(total)
for line in trainFIle:
    words=line.split(' ')
    if str(words[0])=="1":
        one+=1
    elif str(words[0])=="2":
        two+=1
    elif str(words[0])=="3":
        three+=1
    elif str(words[0])=="4":
        four+=1
    else:
        five+=1
    labels.append(words[0])
#accuracyPos()
print(len(labels))
for i in range(len(testline)):

    if str(testline[i].strip())=="1":
        classified_one+=1
    elif str(testline[i].strip())=="2":
        classified_two+=1
    elif str(testline[i].strip())=="3":
        classified_three+=1
    elif str(testline[i].strip())=="4":
        classified_four+=1
    else:
        classified_five+=1

    if str(labels[i])=="1" and str(testline[i].strip())=="1":
        correct_one+=1
    elif str(labels[i])=="2" and str(testline[i].strip())=="2":
        correct_two+=1
    elif str(labels[i])=="3" and str(testline[i].strip())=="3":
        correct_three+=1
    elif str(labels[i])=="4" and str(testline[i].strip())=="4":
        correct_four+=1
    elif str(labels[i])=="5" and str(testline[i].strip())=="5":
        correct_five+=1

print("accuracy is",(correct_one+correct_two+correct_three+correct_four+correct_five)/len(labels))
print("precision and recall for 1",correct_one/classified_one,correct_one/one)
print("precision and recall for 2",correct_two/classified_two,correct_two/two)
print("precision and recall for 3",correct_three/classified_three,correct_three/three)
print("precision and recall for 4",correct_four/classified_four,correct_four/four)
print("precision and recall for 5",correct_five/classified_five,correct_five/five)