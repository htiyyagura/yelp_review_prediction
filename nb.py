import os
import sys
import json
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.cross_validation import train_test_split

def read_json(data_file):
    with open(data_file) as json_data:
        json_list = []
        for line in json_data:
            json_dict = json.loads(line)
            json_list.append(json_dict)
    return json_list

def pre_process(text):
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace("'", '')
    text = text.replace("\"", '')

    tokens = [word for sent in sent_tokenize(text) for word in word_tokenize(sent)]
    #print("1", tokens)
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]
    #print("2", tokens)
    tokens = [word for word in tokens if len(word) >= 3]
    #print("3", tokens)
    tokens = [word.lower() for word in tokens]
    #print("4", tokens)
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    #print("5", tokens)
    return tokens


def process_NB(data=None):
    vectorizer = TfidfVectorizer(tokenizer=pre_process)
    #print("6", vectorizer)
    classifier = MultinomialNB()
    train, test = train_test_split([(i['text'], i['stars']) for i in data],
                                   test_size=.2,
                                   random_state=10)
    #print("train:", train)
    #print("test:", test)
    x_train = vectorizer.fit_transform(i[0] for i in train)
    x_test = vectorizer.transform(i[0] for i in test)
    print("xtrain:", x_train)
    print("xtest:", x_test)
    classifier.fit(x_train, [i[1] for i in train])
    score = classifier.score(x_test, [i[1] for i in test])
    print(score)


def main():
    data = read_json(sys.argv[1])
    if data:
        process_NB(data)
    else:
        print("Source Data is Empty")


if __name__ == '__main__':
    main()