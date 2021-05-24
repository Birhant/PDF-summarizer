"""
Author      :Birhan Tesfaye
Last Edit   :May 23
"""

import PySimpleGUI as sg

def popup_open():
    layout=[
    [sg.Text("PDF file directory :"),sg.Input(key="-PDF_NAME-"),sg.FileBrowse()],
    [sg.Button("Next",key="-READ-")]
    ]
    popup=sg.Window("Open",layout,finalize=True)
    while(True):
        event,values=popup.read()
        pdf_name=None
        if(event==sg.WIN_CLOSED):
            status=False
            break
        if(event is None):
            continue
        elif(event=="-READ-"):
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
    popup=sg.Window("Decrypt",layout,finalize=True)
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

def popup_extractor(doc):
    total=doc.pageCount
    toc=doc.getToC(simple=False)
    doc_text=[]
    status=True
    for i in range(total):
        if(not status):
            break
        page=doc[i]
        status=sg.one_line_progress_meter("Extracting",i+1,total,orientation="h",no_titlebar=True)
        page_text=extract.page(page)
        doc_text.append(page_text)
    return toc,doc_text

def preview(pics):
    current=0
    status=True
    total=len(pics)
    image_data,size=pics[current]
    layout=[
        [sg.Button("Header and footer exist",key="-CHECK-"),sg.Button("Header and footer not found",key="-AGAIN-"),sg.Button("PDF doesnot have header and footer",key="-SKIP-")],
    [sg.Button("Prev",key="-PREV-",size=(5,5)),sg.Image(key="-PREVIEW-",data=image_data,size=size,enable_events=True),sg.Button("Next",key="-NEXT-",size=(5,5))]
    ]
    window=sg.Window('Find header and footer',layout,finalize=True,grab_anywhere=True)
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
        elif(event=="-CHECK-"):
            status=True
            break
        elif(event=="-SKIP-"):
            status=True
            current=-1
            break
        elif(event=="-AGAIN-"):
            status=False
            break
    window.close()
    return status,current
