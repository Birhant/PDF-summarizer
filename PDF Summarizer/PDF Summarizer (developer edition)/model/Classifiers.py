"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import nltk
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier as SGD
from sklearn.svm import SVC,LinearSVC,NuSVC
from nltk.classify.util import accuracy
from model import model

class NaiveBayesClassifier:
    def __init__(self,train_set,test_set,file_name,*args,**kwargs):
        self.test_set=test_set
        self.file_name=file_name
        self.classifier=nltk.NaiveBayesClassifier.train(train_set,*args,**kwargs)
    def test(self):
        return accuracy(self.classifier,self.test_set)
    def write(self):
        return model.write(self.classifier,self.file_name)

class BNBClassifier:
    def __init__(self,train_set,test_set,file_name,*args,**kwargs):
        self.file_name=file_name
        self.classifier=SklearnClassifier(BernoulliNB(),*args,**kwargs)
        self.classifier.train(train_set)
    def test(self):
        pass
    def write(self):
        return model.write(self.classifier,self.file_name)

class LogisticRegressionClassifier:
    def __init__(self,train_set,test_set,file_name,*args,**kwargs):
        self.file_name=file_name
        self.classifier=SklearnClassifier(LogisticRegression(),*args,**kwargs)
        self.classifier.train(train_set)
    def test(self):
        pass
    def write(self):
        return model.write(self.classifier,self.file_name)

class SGDClassifier:
    def __init__(self,train_set,test_set,file_name,*args,**kwargs):
        self.file_name=file_name
        self.classifier=SklearnClassifier(SGD(),*args,**kwargs)
        self.classifier.train(train_set)
    def test(self):
        pass
    def write(self):
        return model.write(self.classifier,self.file_name)
