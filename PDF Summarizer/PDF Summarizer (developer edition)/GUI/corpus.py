"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg

def popup_select_corpus():
    variable=["Headings","Blocks"]
    layout=[
    [sg.Text("Select type of corpus to collect")],
    [sg.Listbox(variable,variable[0],key="-CHOICE-",size=(10,5))],
    [sg.Button("Submit",key="-SUBMIT-")],
    ]
    popup=sg.Window("select",layout,finalize=True)
    while(True):
        event,values=popup.read()
        pdf_name=None
        if(event==sg.WIN_CLOSED):
            status=False
            selected=0
            break
        elif(event=="-SUBMIT-"):
            status=True
            selected=values["-CHOICE-"][0]
            break
    popup.close()
    return status,selected

def popup_select_algorithm():
    variable=["NaiveBayesClassifier","BNBClassifier","LogisticRegressionClassifier","SGDClassifier"]
    layout=[
    [sg.Text("Select type of algorithm to use")],
    [sg.Listbox(variable,variable[0],key="-CHOICE-",size=(10,5))],
    [sg.Button("Submit",key="-SUBMIT-")],
    ]
    popup=sg.Window("select",layout,finalize=True)
    while(True):
        event,values=popup.read()
        pdf_name=None
        if(event==sg.WIN_CLOSED):
            status=False
            selected=0
            break
        elif(event=="-SUBMIT-"):
            status=True
            selected=values["-CHOICE-"][0]
            break
    popup.close()
    return status,selected

def popup_show_model(model):
    layout=[
    [sg.Button("Test",key="-TEST-"),sg.Text("",key="-TEST_VALUE-")],
    [sg.Button("Write",key="-WRITE-"),sg.Text("",key="-WRITE_VALUE-")],
    ]
    popup=sg.Window("Model",layout,finalize=True,size=(100,100))
    while(True):
        event,values=popup.read()
        if(event==sg.WIN_CLOSED):
            break
        elif(event=="-TEST-"):
            test=model.test()
            popup["-TEST_VALUE-"].update(test)
        elif(event=="-WRITE-"):
            write=model.write()
            popup["-WRITE_VALUE-"].update(write)
    popup.close()
