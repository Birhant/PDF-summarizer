"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg
from summarizer import summarizer

def popup_choose():
    ratio_value=[i/10 for i in range(1,10)]
    parameter_tooltip="Ratio refers to percentage to reduce\nword count refers to desired number of words"
    layout=[
    [sg.Combo(["Ratio"],"Ratio",readonly=True,tooltip=parameter_tooltip,enable_events=True,key="-LIST-",size=(20,2))
     ,sg.Input(key="-VALUE_OTHER-",size=(5,1),visible=False),sg.Spin(ratio_value,key="-VALUE_RATIO-")],
    [sg.Button("Summarize",key="-SUMMARIZE-")],
    ]
    popup=sg.Window("Choose summarizer",layout,finalize=True,modal=True)
    while(True):
        event,values=popup.read()
        pdf_name=None
        if(event==sg.WIN_CLOSED):
            status=False
            break
        if(event is None):
            continue
        elif(event=="-LIST-"):
            if(values["-LIST-"]=="Ratio"):
                popup["-VALUE_RATIO-"].update(visible=True)
                popup["-VALUE_OTHER-"].Update(visible=False)
            else:
                popup["-VALUE_RATIO-"].Update(visible=False)
                popup["-VALUE_OTHER-"].Update(visible=True)
        elif(event=="-SUMMARIZE-"):
            status=True
            if(values["-LIST-"].startswith("Ratio")):
                value={"ratio":float(values["-VALUE_RATIO-"])}
                summarize=summarizer.ratio
            else:
                value={"word_count":int(values["-VALUE_OTHER-"])}
                summarize=summarizer.word_count
            break
    popup.close()
    return status,summarize,value

def popup_save():
    layout=[
    [sg.Text("Output file directory :"),sg.Input(key="-FILE_NAME-",enable_events=True),sg.FileSaveAs(file_types=(('ALL Files', '*.txt'),))],
    [sg.Button("Finish",key="-WRITE-")]
    ]
    popup=sg.Window("Save",layout,finalize=True,modal=True)
    popup['-FILE_NAME-'].bind('<Return>','SET')
    while(True):
        event,values=popup.read()
        file_name=None
        if(event==sg.WIN_CLOSED):
            status=False
            break
        if(event is None):
            continue
        elif(event=="-WRITE-" or event=="-FILE_NAME-SET"):
            status=True
            file_name=values["-FILE_NAME-"]
            break
    popup.close()
    return status,file_name
