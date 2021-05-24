"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg
from pdf import extract
from pdf import natural_order

def popup_open():
    layout=[
    [sg.Text("PDF file directory :"),sg.Input(key="-PDF_NAME-",enable_events=True),sg.FileBrowse()],
    [sg.Button("Next",key="-READ-")]
    ]
    popup=sg.Window("Open",layout,finalize=True,modal=True)
    popup['-PDF_NAME-'].bind('<Return>','SET')
    while(True):
        event,values=popup.read()
        pdf_name=None
        if(event==sg.WIN_CLOSED):
            status=False
            break
        if(event is None):
            continue
        elif(event=="-READ-" or event=="-PDF_NAME-SET"):
            status=True
            pdf_name=values["-PDF_NAME-"]
            break
    popup.close()
    return status,pdf_name

def popup_decrypt():
    layout=[
    [sg.Text("Password"),sg.Input(key="-PASSWORD-")],
    [sg.Button("Next",key="-DECRYPT-")]
    ]
    popup=sg.Window("Decrypt",layout,finalize=True,modal=True)
    while(True):
        event,values=popup.read()
        status=False
        if(event==sg.WIN_CLOSED):
            break
        if(event is None):
            continue
        elif(event=="-DECRYPT-"):
            status=True
            break
    password=values["-PASSWORD-"]
    popup.close()
    return status,password
    
def popup_progress(current,total,process_title="Work in progress"):
    status=sg.one_line_progress_meter(process_title,current,total,orientation="h",no_titlebar=True)
    return status

def popup_progress_iterate(data,func,process_title="Work in progress"):
    output=[]
    status=True
    for i in data:
        if(not status):
            break
        new=func(i)
        status=sg.one_line_progress_meter(process_title,i+1,total,orientation="h",no_titlebar=True)
        output.append(new)
    else:
        status=True
    return status,output

def popup_header_footer(pics):
    index=0
    current=0
    total=len(pics)
    image_data,size=pics[current]
    header_footer=["Neither Header nor Footer","Only Header","Only Footer","Header and Footer"]
    status=True

    layout=[
    [sg.Button("Try other pages",key="-AGAIN-"),sg.Combo(header_footer,header_footer[0],readonly=True,key="-CHECK-"),sg.OK()],
    [sg.Button("Prev",key="-PREV-",size=(5,5)),sg.Image(key="-PREVIEW-",data=image_data,size=size),sg.Button("Next",key="-NEXT-",size=(5,5))]
    ]
    window=sg.Window('Locate header and footer',layout,finalize=True,grab_anywhere=True,modal=True,location=(100,0))
    while(True):
        event,values=window.read()
        if(event==sg.WIN_CLOSED or event=="-PREVIEW-"):
            break
        if(event=='-NEXT-'):
            current=0 if current==total-1 else current+1
            image_data,size=pics[current]
            window["-PREVIEW-"].update(data=image_data,size=size)
        elif(event=='-PREV-'):
            current=total-1 if current==0 else current-1
            image_data,size=pics[current]
            window["-PREVIEW-"].update(data=image_data,size=size)
        elif(event=="-PREVIEW-"):
            status=True
            break
        elif(event=="OK"):
            selected=values["-CHECK-"]
            index=header_footer.index(selected)
            status=True
            break
        elif(event=="-AGAIN-"):
            status=False
            break
    window.close()
    return status,current,index