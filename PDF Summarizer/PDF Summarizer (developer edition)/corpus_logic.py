"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from GUI import corpus
from GUI import pdf
from pdf import reader
from corpus import collect_corpus
from corpus import collect_corpus

class Reader:
    def __init__(self):
        self.PDF_obj=reader.Read()
        self.finish=False
        self.step_1()
    def step_1(self):
        status,pdf_name=pdf.popup_open()
        if(status):
            self.PDF_obj.pdf_name=pdf_name
            self.PDF_obj.open()
            if(self.PDF_obj.status):
                self.step_2()
            else:
                self.step_1()
    def step_2(self):
        status=False
        if(self.PDF_obj.encrypted):
            status,password=pdf.popup_decrypt()
        if(status):
            status=self.PDF_obj.decrypt(password)
            if(not status):
                self.step_2()
        self.finish=True

class Collect:
    def __init__(self,doc):
        self.doc=doc
        self.step_1()
    def step_1(self):
        status,selected=corpus.popup_select_corpus()
        if(status):
            if(selected=="Headings"):
                self.obj=collect_corpus.Headings(self.doc)
            else:
                self.obj=collect_corpus.Blocks(self.doc)
        else:
            self.step_1()
        self.obj.GUI()


