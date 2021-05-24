"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg
import corpus_logic
import train_logic
layout=[
    [
        sg.Button("Collect corpus",key="-CORPUS-"),sg.Button("Train model",key="-TRAIN-")]
    ]
window=sg.Window("TBS",layout,finalize=True)
while(True):
    event,values=window.read()
    if(event==sg.WIN_CLOSED):
        break
    if(event is None):
        continue
    if(event=="-CORPUS-"):
        read=corpus_logic.Reader()
        if(read.finish):
            collect=corpus_logic.Collect(read.PDF_obj.doc)
    if(event=="-TRAIN-"):
        train=train_logic.Train()

    

window.close()
