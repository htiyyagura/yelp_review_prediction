import random
vocab_dict = {}
#feat = [[0 for i in range(24878)] for y in range(5)]
#print(feat[0][36844])
def vocab_count():
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
    print(len(vocab_dict.items()))
    init_dict(len(vocab_dict.items()))

def init_dict(x):
    feat = [[0 for i in range(x)] for y in range(5)]
    feat_avg = [[0 for i in range(x)] for y in range(5)]
    gen_model(feat,feat_avg)


def split_data():
    fr = open('yelp_shuffled','r')
    fw1 = open('train75_18750_bi','w')
    fw2 = open('test25_7250_bi','w')

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


def gen_model(feat,feat_avg):
    global vocab_dict
    sum_weights = []


    fr = open('train75_18750_bi','r')
    lines = fr.readlines()
    for i in range(0,4):
        random.shuffle(lines)
        wrong = 0
        for j in range(0,len(lines)):
            label = int(lines[j][0])

            sum_weights = [0 for i in range(5)]
            #print(sum_weights)
            indices =[]
            line = lines[j].split()
            for k in range(1,len(line)):
                sublist = []
                sublist = line[k].split(':')
                #print("sublist")
                #print(sublist)
                for l in range(0,5):
                    #feat[l][int(sublist[0])] *= int(sublist[1])
                    sum_weights[l] += feat[l][int(sublist[0])-1]
                    indices.append(int(sublist[0])-1)
                pred = sum_weights.index(max(sum_weights))
                #print("max weight",max(sum_weights))
            if label != pred+1:
                for x in range(0,len(indices)):
                    feat[pred][indices[x]] -= 1
                    feat[label-1][indices[x]] +=1
                    feat_avg[pred][indices[x]]+=feat[pred][indices[x]]
                    feat_avg[label-1][indices[x]]+=feat[label-1][indices[x]]

                wrong += 1


        print("error rate",wrong/18750)
    fr.close()

    classify(feat)

def classify(feat):

    c = 0
    fr = open("test25_7250_bi",'r')
    fw = open('opfile','w')
    lines = fr.readlines()
    for i in range(0,len(lines)):
        line = lines[i].split()
        sum_weights = [0 for i in range(5)]
        for j in range(0,len(line)):
            sublist = line[j].split(':')
            for k in range(0,5):
                #feat[l][int(sublist[0])] *= int(sublist[1])
                sum_weights[k] += feat[k][int(sublist[0])-1]
        pred = sum_weights.index(max(sum_weights))
        lab = pred+1
        fw.write(str(lab)+'\n')
        if lab == line[0]:
            c = c+1

    print('acc',c/6251)
    fr.close()
    fw.close()

def cal_acc():
    c = 0
    fr1 = open('test25_7250_bi','r')
    fr2 = open('opfile','r')
    lines1 = fr1.readlines()
    lines2 = fr2.readlines()
    for i in range(0,len(lines1)):
        if lines1[i][0] == lines2[i][0]:
            c = c+1
    print('acc',c/6251)



def start():
    split_data()
    vocab_count()
    gen_model()
    classify()
    cal_acc()

start()
