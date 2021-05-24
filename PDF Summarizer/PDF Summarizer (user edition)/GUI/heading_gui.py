"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg

class Valid:
    def __init__(self,doc,lvl=1):
        self.toc=doc.getToC(simple=False)
        self.total_page=doc.pageCount
        self.headings=[]
        for i,value in enumerate(self.toc):
            if(value[0]==lvl):
                self.headings.append((value[1],i))
        self.GUI()

    def place_headings(self):
        frame_layout=[]
        self.index=[]
        for i,value in enumerate(self.headings):
            self.index.append(i)
            widget=[sg.Text(str(i)+"\t"+value[0])]
            frame_layout.append(widget)
        self.index.append(len(self.index))
        return frame_layout

    def GUI(self):
        self.valid=None
        frame_layout=self.place_headings()
        layout=[
            [sg.Frame("Headings",frame_layout)],
            [sg.Text("Valid headings from start"),sg.Spin(self.index,0,key="-START-"),sg.Text("TO"),sg.Spin(self.index,self.index[-1],key="-END-"),sg.Button("Submit",key="-SUBMIT-")]
            ]
        window = sg.Window("Headings to be used", layout,default_element_size=(12,1))
        while True:
            event, values = window.read()
            if(event == sg.WIN_CLOSED):
                break
            elif(event == "-SUBMIT-"):
                if(values["-START-"]<values["-END-"]):
                    first=self.headings[values["-START-"]][1]
                    if(len(self.headings)==values["-END-"]):
                        last=len(self.toc)
                        self.last_page=self.total_page
                    else:
                        last=self.headings[values["-END-"]][1]
                        self.last_page=self.toc[last][2]
                    self.valid=self.toc[first:last]
                    break
        window.close()
