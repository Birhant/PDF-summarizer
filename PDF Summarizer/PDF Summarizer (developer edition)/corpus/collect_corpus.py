"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import fitz
from PIL import Image
import json
import PySimpleGUI as sg
import io
import os

class Blocks:
    def __init__(self,doc):
        self.doc = doc
        self.max_pno=self.doc.pageCount
        self.max_block=0
        self.current_pno=-1
        self.current_block=0
        self.blocks=None
        self.page=None

    def strip(self,text):
        List=text.split(' ')
        for i in List.copy():
            if(i==""):
                List.remove(i)
        text=" ".join(List)
        text=text.strip().lower()
        return text

    def increment(self):
        pix=None
        if(self.current_pno<self.max_pno-1):
            if(self.current_block>=self.max_block-1):
                self.current_pno+=1
                self.page=self.doc.loadPage(self.current_pno)
                text=self.page.getText("json")
                pgdict=json.loads(text)
                self.blocks=pgdict["blocks"]
                self.max_block=len(self.blocks)
                self.current_block=0
            else:
                self.current_block+=1
            rect=self.blocks[self.current_block]['bbox']
            block=fitz.Rect(rect)
            mat = fitz.Matrix(2, 2)
            pix = self.page.getPixmap(matrix=mat, clip=block)
            mode = "RGBA" if pix.alpha else "RGB"
            image = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        return image

    def GUI(self):
        layout=[
            [sg.Image(key="-IMAGE-")],
            [sg.Button("Prev",key="-PREV-"),sg.Button("Next",key="-NEXT-"),sg.Button("Next block",key="-NEXT_BLOCK-"),sg.Button("Next page",key="-NEXT_PAGE-"),sg.Radio("Invalid","category",key="-INVALID-"),sg.Radio("Valid","category",key="-VALID-"),sg.Button("Select",key="-SELECT-")],
            [sg.Button("Exit",key="-EXIT-")],
            ]
        window = sg.Window("Image Viewer", layout,default_element_size=(12,1))
        while True:
            event, values = window.read()
            if(event == sg.WIN_CLOSED):
                break
            if(event == "-NEXT_PAGE-"):
                self.current_pno+=2
                bio = io.BytesIO()
                image=self.increment()
                if(image is not None):
                    image.save(bio, format="PNG")
                    window["-IMAGE-"].update(data=bio.getvalue())
                else:
                    break
            elif(event == "-NEXT_BLOCK-"):
                self.current_block+=1
                bio = io.BytesIO()
                image=self.increment()
                if(image is not None):
                    image.save(bio, format="PNG")
                    window["-IMAGE-"].update(data=bio.getvalue())
                else:
                    break
            elif(event == "-NEXT-"):
                bio = io.BytesIO()
                image=self.increment()
                if(image is not None):
                    image.save(bio, format="PNG")
                    window["-IMAGE-"].update(data=bio.getvalue())
                else:
                    break
            elif(event == "-SELECT-"):
                if(values['-VALID-']):
                    self.write('valid')
                else:
                    self.write('invalid')
                break
            elif(event == "-EXIT-"):
                break
        window.close()

    def naming(self,mode):
        dir="corpus/block/"+mode
        files=os.listdir(dir)
        name=''
        no=len(files)
        name=mode+"_"+str(no)+".txt"
        return dir+"/"+name


    def write(self,mode):
        file_name=self.naming(mode)
        text=self.selected()
        with open(file_name,'w',encoding='utf-8') as writer:
            writer.write(text)

    def selected(self):
        text=""
        block=self.blocks[self.current_block]
        if("text" in block.keys()):
            text+=block['text']
        elif("lines" in block.keys()):
            for line in block["lines"]:
                if("spans" in line.keys()):
                    for span in line['spans']:
                        text+=span['text']+' '
        text=self.strip(text)
        return text

class Headings:
    def __init__(self,doc):
        self.valid_dir="corpus/heading/valid.txt"
        self.invalid_dir="corpus/heading/invalid.txt"
        toc=doc.getToC()
        self.headings=[]
        for i in toc:
            if(i[0]==1):
                self.headings.append(i[1])

    def place_headings(self):
        frame_layout=[]
        self.index=[]
        for i,index in enumerate(self.headings):
            self.index.append(i)
            widget=[sg.Text(str(i)+"\t"+index)]
            frame_layout.append(widget)
        self.index.append(len(self.index))
        return frame_layout

    def GUI(self):
        frame_layout=self.place_headings()
        layout=[
            [sg.Frame("Headings",frame_layout)],
            [sg.Text("Valid headings from start"),sg.Spin(self.index,0,key="-START-"),sg.Text("TO"),sg.Spin(self.index,self.index[-1],key="-END-"),sg.Button("Submit",key="-SUBMIT-")]
            ]
        window = sg.Window("Train Heading", layout,default_element_size=(12,1))
        while True:
            event, values = window.read()
            if(event == sg.WIN_CLOSED):
                break
            elif(event == "-SUBMIT-"):
                if(values["-START-"]<values["-END-"]):
                    valid='\n'.join(self.headings[values["-START-"]:values["-END-"]])
                    invalid='\n'.join(self.headings[0:values["-START-"]]+self.headings[values["-END-"]:])
                    valid+="\n"
                    invalid+="\n"
                    self.write(valid,self.valid_dir)
                    self.write(invalid,self.invalid_dir)
                    break
        window.close()

    def write(self,text,file_name):
        text=text.lower()
        with open(file_name,'a',encoding='utf-8') as writer:
            writer.write(text)

