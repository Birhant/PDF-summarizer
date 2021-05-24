"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from nltk.probability import FreqDist

def generate_train_set(corpus,limit=0.9):
    documents=[]
    for category in corpus.categories():
        for fileid in corpus.fileids(category):
            words=corpus.words(fileid)
            value=(list(words),category)
            documents.append(value)

    feature_sets=[]
    for text,category in documents:
        bag_of_words=bagOFwords(text)
        feature=(bag_of_words,category)
        feature_sets.append(feature)
    size=len(feature_sets)
    last=int(size*limit)
    train_set=feature_sets[:last]
    test_set=feature_sets[last:]
    return train_set,test_set

def bagOFwords(document):
    features={}
    for word in document:
        features[word]=True
    return features
