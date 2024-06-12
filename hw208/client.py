import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

port = "8050"
ip_address = "127.0.0.1"
SERVER = NONE
BUFFER_SIZE =4096

def musicWindow():
    window = Tk()
    window.title("music app")
    window.geometry("300x300")

    selectLabel = Label(window,text="select song!",bg="blue")
    selectLabel.place(x=2,y=2)

    listbox = Listbox(window,height=40,width=40,activestyle="dotbox")
    listbox.place(x=10,y=10)

    scrollbarList =  Scrollbar(listbox)
    scrollbarList.place(relheight=1,relx=1)
    scrollbarList.config(command= listbox.yview)
    
    playButton = Button(window,text="Play!",width=10,bd=1,bg="blue")
    playButton.place(x=30,y=200)

    stopButton = Button(window,text="Stop!",width=10,bg="blue")
    stopButton.place(x=200,y=200)

    uploadButton = Button(window,text="Upload!",width=10,bg="blue")
    uploadButton.place(x=30,y=250)

    DownloadButton = Button(window,text="Download!",width=10,bg="blue")
    DownloadButton.place(x=4,y=250)

    infoLabel = Label(window,text="",fg="blue")
    infoLabel.place(x=4,y=230)

    window.mainloop()

def setup():
    global SERVER
    global port 
    global ip_address

    musicWindow()
    
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((ip_address,port))
setup()