"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import random
import json
from pdf import natural_order

def previewer(doc):
    no=doc.pageCount
    pnos=[]
    for i in range(10):
        pnos.append(random.randrange(0,no,10))
    pics=[]
    for i in pnos:
        page=doc[i]
        pix=page.getPixmap()
        size=(pix.width,pix.height)
        image_data=pix.getImageData("ppm")
        pics.append((image_data,size))
    return pics,pnos

def header_footer(page,status):
    text=page.getText("json")
    pgdict=json.loads(text)
    page_text=pgdict["blocks"]
    blocks=natural_order.SortBlocks(page_text)
    if(status==1):
        header=blocks[0]['bbox']
        footer=(0,0,0,0)
    elif(status==2):
        header=(0,0,0,0)
        footer=blocks[-1]['bbox']
    elif(status==3):
        header=blocks[0]['bbox']
        footer=blocks[-1]['bbox']
    else:
        header=(0,0,0,0)
        footer=(0,0,0,0)
    return header,footer

def locate_header_footer(page,header_footer):
    header,footer=header_footer
    text=page.getText("json")
    pgdict=json.loads(text)
    page_text=pgdict["blocks"]
    blocks=natural_order.SortBlocks(page_text)
    if(header==(0,0,0,0)):
        del blocks[0]
    if(footer==(0,0,0,0)):
        del blocks[-1]
    return blocks
