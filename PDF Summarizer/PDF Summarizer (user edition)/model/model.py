"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import pickle

def read(file_name,directory='model'):
    path=directory+'/'+file_name+'.pickle'
    try:
        with open(path,'rb')as reader:
            obj=pickle.load(reader)
    except Exception:
        obj=None
    return obj

def write(obj,file_name,directory='model'):
    path=directory+'/'+file_name+'.pickle'
    try:
        with open(path,'wb')as writter:
            pickle.dump(obj,writter)
            status=True
    except Exception:
        status=False
    return status
