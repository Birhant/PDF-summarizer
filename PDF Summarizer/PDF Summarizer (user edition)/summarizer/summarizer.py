"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from gensim.summarization import summarizer
from summarizer import tokenizer

def check_text_size(text):
    tokenized,text_type=tokenizer.nltk_original(text)
    if(text_type == 'word' or text_type == 'sent'):
        status=False
    else:
        status=True
    return status

def check_summary(summarized,original):
    if(summarized==""):
        summarized=original
    return summarized

def word_count(text,word_count=100):
    status=check_text_size(text)
    if(status):
        try:
            summarized=summarizer.summarize(text,word_count=word_count)
        except Exception:
            summarized=text
    else:
        summarized=text
    summarized=check_summary(summarized,text)
    return summarized

def ratio(text,ratio=0.2):
    summarized=text
    status=check_text_size(text)
    if(status):
        try:
            summarized=summarizer.summarize(text,ratio=ratio)
        except Exception:
            summarized=text            
    summarized=check_summary(summarized,text)
    return summarized

def pdf(doc_text,summarizer,**parameter):
    summarized_doc=[]
    for page in doc_text:
        summarized_page=[]
        for block in page:
            if(block[1].startswith("heading")):
                summarized=block[0]
            else:
                summarized=summarizer(block[0],**parameter)
            summarized_page.append((summarized,block[1]))
        summarized_doc.append(summarized_page)
    return summarized_doc
