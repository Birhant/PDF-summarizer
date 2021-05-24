"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import blankline_tokenize
"""
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import line_tokenize
from nltk.util import bigrams,trigrams,ngrams
"""
from summarizer import structure

word_tokenizer=nltk.word_tokenize
sent_tokenizer=nltk.sent_tokenize
para_tokenizer=blankline_tokenize

def nltk_original(corpus):
    struct=structure.Structure
    funcs={
        'word_func':nltk.word_tokenize,
        'sent_func':nltk.sent_tokenize,
        'para_func':blankline_tokenize,
        'page_func':RegexpTokenizer('\n\n',gaps=True).tokenize
        }
    tokenized,text_type=struct.run(corpus,**funcs)
    return tokenized,text_type

def Regexp_based(corpus):
    struct=structure.Structure
    funcs={
        'word_func':RegexpTokenizer('\s+',gaps=True).tokenize,
        'sent_func':RegexpTokenizer('. ',gaps=True).tokenize,
        'para_func':RegexpTokenizer('\n',gaps=True).tokenize,
        'para_func':RegexpTokenizer('\n\n',gaps=True).tokenize
        }
    tokenized,text_type=struct.run(corpus,**funcs)
    return tokenized,text_type
