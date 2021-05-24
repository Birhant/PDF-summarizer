"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

def concat(doc):
    String=""
    for page in doc:
        for block in page:
            String+=' '+block[0]
        String+="\n"
    return String

def write(text,directory):
    text=concat(text)
    with open(directory,'w',encoding="utf-8") as writer:
        writer.write(text)
