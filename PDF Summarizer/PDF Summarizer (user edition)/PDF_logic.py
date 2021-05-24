"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from GUI import pdf_gui
from GUI import heading_gui
from GUI import summarizer_gui
from pdf import reader
from pdf import header_and_footer
from pdf import extract
from model import Classifier
from summarizer import summarizer
from output import text

class Reader:
    def __init__(self):
        print("Reading")
        self.status=True
        self.PDF_obj=reader.Read()
        self.step_1()

    def step_1(self):
        status,pdf_name=pdf_gui.popup_open()
        if(status):
            self.PDF_obj.pdf_name=pdf_name
            self.PDF_obj.open()
            if(self.PDF_obj.status):
                self.step_2()
            else:
                self.step_1()
        else:
            self.status=False

    def step_2(self):
        if(self.PDF_obj.encrypted):
            state,password=pdf_gui.popup_decrypt()
            if(state):
                state=self.PDF_obj.decrypt(password)
                if(not state):
                    self.step_2()
            else:
                self.status=False

class Preprocessor:
    def __init__(self,doc):
        print("cleaning")
        self.doc=doc
        self.status=True
        self.step_1()

    def step_1(self):
        pics,pnos=header_and_footer.previewer(self.doc)
        status,pno,index=pdf_gui.popup_header_footer(pics)
        if(status):
            pno=pnos[index]
            self.header_footer=header_and_footer.header_footer(self.doc[pno],index)
            self.step_2()
        else:
            self.step_1()

    def step_2(self):
        try:
            valid_heading=heading_gui.Valid(self.doc)
            self.headings=valid_heading.valid
            last_page=valid_heading.last_page
            self.start=self.headings[0][2]-1
            self.end=last_page
            self.step_3()
        except Exception:
            self.status=False

    def step_3(self):
        self.current=0
        self.doc_text=[]
        try:
            for i in range(self.start,self.end):
                page=self.doc[i]
                blocks=header_and_footer.locate_header_footer(page,self.header_footer)
                page_text=[]
                for block in blocks:
                    if(block["type"]==1):
                        continue
                    text=extract.extractor(block,self.headings[self.current])
                    if(text[1].startswith('heading')):
                        self.current+=1
                    page_text.append(text)
                self.doc_text.append(page_text)
        except Exception:
            self.status=False

class Summarizer:
    def __init__(self,doc_text):
        print("Summarizing")
        self.doc_text=doc_text
        self.status=True
        self.summarized_doc=None
        self.step_1()

    def step_1(self):
        status,summarizer_func,value=summarizer_gui.popup_choose()
        if(status):
            self.summarized_doc=summarizer.pdf(self.doc_text,summarizer_func,**value)
        else:
            self.status=False

class Output:
    def __init__(self,summarized_text):
        print("Writing")
        self.summarized_text=summarized_text
        self.status=True
        self.step_1()

    def step_1(self):
        status,directory=summarizer_gui.popup_save()
        if(status):
            text.write(self.summarized_text,directory)
        else:
            self.status=False

