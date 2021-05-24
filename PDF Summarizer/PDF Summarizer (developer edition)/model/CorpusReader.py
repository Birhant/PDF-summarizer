"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from nltk.corpus.reader import WordListCorpusReader,CategorizedCorpusReader
from nltk.corpus.reader import CategorizedPlaintextCorpusReader

class CategorizedWordlistCorpusReader(CategorizedCorpusReader,WordListCorpusReader):
    def __init__(self, *args, **kwargs):
        CategorizedCorpusReader.__init__(self, kwargs)
        WordListCorpusReader.__init__(self, *args, **kwargs)
    def _resolve(self, fileids, categories):
        if fileids is not None and categories is not None:
            raise ValueError('Specify fileids or categories, not both')
        if categories is not None:
            return self.fileids(categories)
        else:
            return fileids

def Heading_corpus_reader():
    reader=CategorizedWordlistCorpusReader("corpus/heading", r'.*\.txt',
        cat_pattern=r'(\w+)\.txt')
    return reader

def Block_corpus_reader():
    reader = CategorizedPlaintextCorpusReader('corpus/block', r'.*/.*\.txt',
    cat_pattern=r'(\w+)/.*\.txt')
    return reader

