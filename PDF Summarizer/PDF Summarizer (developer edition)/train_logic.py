"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from GUI import corpus
from model import CorpusReader
from model import Feature
from model import Classifiers

class Train:
    def __init__(self):
        self.file_name=""
        self.step_1()

    def step_1(self):
        status,selected=corpus.popup_select_corpus()
        if(status):
            if(selected=="Headings"):
                self.file_name+="Headings_"
                self.reader=CorpusReader.Heading_corpus_reader()
            else:
                self.file_name+="Blocks_"
                self.reader=CorpusReader.Block_corpus_reader()
        else:
            self.step_1()
        self.step_2()

    def step_2(self):
        self.classifiers_list={
            "NaiveBayesClassifier":Classifiers.NaiveBayesClassifier,
            "BNBClassifier":Classifiers.BNBClassifier,
            "LogisticRegressionClassifier":Classifiers.LogisticRegressionClassifier,
            "SGDClassifier":Classifiers.SGDClassifier
        }
        self.train_set,self.test_set=Feature.generate_train_set(self.reader)
        status,selected=corpus.popup_select_algorithm()
        if(status):
            self.file_name+=selected
            classifier=self.classifiers_list[selected]
        else:
            self.step_2()
        self.classifier=classifier(self.train_set,self.test_set,self.file_name)
        self.step_3()

    def step_3(self):
        corpus.popup_show_model(self.classifier)
        


