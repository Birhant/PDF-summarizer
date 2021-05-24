"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

from pdf import font
from pdf import natural_order
import json
SortBlocks=natural_order.SortBlocks
SortLines=natural_order.SortLines
SortSpans=natural_order.SortSpans

heading_name=["chapter","unit","part"]
heading_lvl=["zero","one","two","three","four","five","six","seven","eight","nine","ten","0","1","2","3","4","5","6","7","8","9"]
heading_sep=[" ",":"]
def remove_empty(List):
    for i in List.copy():
        if(i[0].strip()==""):
            List.remove(i)

def identify_heading(txt,toc):
    status=False
    title=toc[1].lower()
    text=txt[0].lower()
    title=title.strip()
    if(title==text):
        status=True
    return status

def identify_heading_name(txt):
    status=False
    text=txt.lower()
    current_name=0
    current_lvl=0
    current_sep=0
    while(True):
        heading=heading_name[current_name]+heading_sep[current_sep]+heading_lvl[current_lvl]
        if(text==heading):
            status=True
        else:
            current_sep+=1
            if(current_sep==len(heading_sep)):
                current_sep=0
                current_lvl+=1
            if(current_lvl==len(heading_lvl)):
                current_lvl=0
                current_name+=1
            if(current_name==len(heading_name)):
                break
    return status

def average(List):
    total=0
    for i in List:
        total+=i[1]
        average=total//len(List)
    return average

def get_text(List):
    text=''
    for i in List:
        text+=i[0]+' '
    text=text.strip()
    return text

def extractor(block,toc):
    if("lines" in block.keys()):
        lines=SortLines(block["lines"])
        ln_text=[]
        for line in lines:
            if("spans" in line.keys()):
                spans=SortSpans(line["spans"])
                for span in spans:
                    text=span['text']
                    size=span["size"]
                    flag=font.flags_decomposer(span["flags"])
                    ln_text.append((text,size,flag))
        size=average(ln_text)
        remove_empty(ln_text)
        text=get_text(ln_text)
        text_type='content'
        status=identify_heading_name(text)
        if(status):
            text_type="delete"
        else:
            is_header=identify_heading((text,size,flag),toc)
            if(is_header):
                text_type="heading_"+str(toc[0])
    return [text,text_type]

                

