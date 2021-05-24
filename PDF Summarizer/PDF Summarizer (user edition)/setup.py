"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg
import PDF_logic
from summarizer import summarizer
from GUI import summarizer_gui

ratio_value=[i/10 for i in range(1,10)]
parameter_tooltip="Ratio refers to percentage to reduce\nword count refers to desired number of words"
layout=[
    [sg.Button("Summarize textbook",key="-PDF_SUMMARIZER-"),sg.Button("Keyword based summarizer",key="-KEYWORD-"),sg.Button("Normalize PDF",key="-PDF_NORMALIZER-")],
    [sg.Combo(["Ratio","word count"],"Ratio",readonly=True,tooltip=parameter_tooltip,enable_events=True,key="-LIST-",size=(20,2))
     ,sg.Input(key="-VALUE_WORD_COUNT-",size=(5,1),visible=False),sg.Spin(ratio_value,key="-VALUE_RATIO-")],
    [sg.Button("Summarize",key="-SUMMARIZE-")],
    [sg.Multiline(key="-INPUT-",size=(50,100),autoscroll=True),sg.Multiline(key="-OUTPUT-",size=(50,100))],
    ]
sg.theme("Dark Blue 3")
window=sg.Window("TBS",layout,finalize=True,size=(1000,600))
while(True):
    event,values=window.read()
    if(event==sg.WIN_CLOSED):
        break
    elif(event is None):
        continue
    elif(event=="-PDF_SUMMARIZER-"):
        read=PDF_logic.Reader()
        if(read.status):
            clean=PDF_logic.Preprocessor(read.PDF_obj.doc)
            if(clean.status):
                summary=PDF_logic.Summarizer(clean.doc_text)
                if(summary.status):
                    output=PDF_logic.Output(summary.summarized_doc)

    elif(event=="-LIST-"):
        if(values["-LIST-"]=="Ratio"):
            window["-VALUE_RATIO-"].update(visible=True)
            window["-VALUE_WORD_COUNT-"].Update(visible=False)
        else:
            window["-VALUE_RATIO-"].Update(visible=False)
            window["-VALUE_WORD_COUNT-"].Update(visible=True)
            
    elif(event=="-SUMMARIZE-"):
        if(values["-LIST-"][0].startswith("Ratio")):
            value=float(values["-VALUE_RATIO-"])
            summarized=summarizer.ratio(values["-INPUT-"],value)
        else:
            value=int(values["-VALUE_WORD_COUNT-"])
            summarized=summarizer.ratio(values["-INPUT-"],value)
        window["-OUTPUT-"].update(value=summarized)
        window["-INPUT-"].update(value="")


    

window.close()
