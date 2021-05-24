"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from model import model
class Classifier:
    def __init__(self,file_name):
        self.classifier=model.read(file_name)
        print(self.classifier)
    def classify(self,text):
        features=self.bagofwords(text)
        category=self.classifier.classify(features)
        return category
    def bagofwords(self,text):
        feature={}
        for word in text:
            word=word.lower()
            feature[word]=True
        return feature
