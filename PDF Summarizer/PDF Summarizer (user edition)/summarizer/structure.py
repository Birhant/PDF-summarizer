"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

class Structure:
    def textTypes():
        t_types=['word','sent','para','page']
        return t_types

    def noChange(value):
        return value

    def setDefaultfuncs(funcs):
        text_types=Structure.textTypes()
        for text_type in text_types:
            key=text_type+'_func'
            funcs.setdefault(key,Structure.noChange)
        return funcs,text_types

    def iterate(corpus,text_types,index,**funcs):
        if(index>0 and isinstance(corpus,list)):
            for i in range(len(corpus)):
                corpus[i]=Structure.apply(corpus[i],text_types[index-1],True,**funcs)
        return corpus
        
    def apply(corpus,text_type,applyONcurrent=True,**funcs):
        text_types=Structure.textTypes()
        index=text_types.index(text_type)
        if(applyONcurrent):
            key=text_type+'_func'
            func=funcs[key]
            corpus=func(corpus)
            corpus=Structure.iterate(corpus,text_types,index,**funcs)
        else:
            corpus=Structure.apply(corpus,text_types[index-1],True,**funcs)
        return corpus

    def do(corpus,text_type,**funcs):
        funcs,text_types=Structure.setDefaultfuncs(funcs)
        corpus=Structure.apply(corpus,text_type,**funcs)
        return corpus

        
    def run(corpus,text_type=None,applyONcurrent=False,**funcs):
        funcs,text_types=Structure.setDefaultfuncs(funcs)
        if(text_type not in text_types):
            text_type=Structure.detect(corpus,**funcs)
        corpus=Structure.apply(corpus,text_type,applyONcurrent,**funcs)
        return corpus,text_type

    def detect(corpus,**funcs):
        default='page'
        text_types=Structure.textTypes()
        for t_type in text_types:
            key=t_type+'_func'
            func=funcs[key]
            new_corpus=func(corpus)
            if(isinstance(new_corpus,list) and len(new_corpus)==1):
                text_type=t_type
                break
        else:
            text_type=default
        return text_type
