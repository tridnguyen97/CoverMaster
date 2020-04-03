'''Please Note: this is a very noobish script that i wrote to download a coverr art from spotify or soundcloud and then embeds them to your MP3 files. 
This is my first script where i used python GUI programming. Suggestion and Criticisms are warmly welcome'''

import re
import requests
import threading
import webbrowser
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox  
from mutagen.id3 import ID3, APIC, error


def changer():
    #create window object
    root1 = tk.Toplevel(root)

    #remove the maximize button
    # root1.resizable(0,0)

    #title, window resolution of the main window
    root1.geometry('400x300')
    root1.title('Cover Art Changer')

    # get cover image location 
    def image():
        global x
        x = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("jpeg files","*.jpg")])
        if x:
            global label1
            v = StringVar()
            label1 = Label(root1, textvariable=v)
            v.set(x)
            label1.pack(pady=(10,0))

    # get MP3 file location      
    def audio():
        global y
        y = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("mp3 files","*.mp3")])
        if y:
            global label2
            v = StringVar()
            label2 = Label(root1, textvariable=v)
            v.set(y)
            label2.pack(pady=(10,0))

    # add album art to the MP3 file
    # got this from https://www.codespeedy.com/add-album-art-to-an-mp3-file-in-python/
    def job():
        audio = MP3(y, ID3=ID3)
        try:
            audio.add_tags()
        except error:
            pass

        audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=open(x,'rb').read()))
        audio.save()  
        global label3
        label3 = ttk.Label(root1, text="Cover art changed successfully")
        label3.pack()

    # function of the clear button [button4]
    def clear():
        label1.pack_forget()
        label2.pack_forget()
        label3.pack_forget()

    button1 = ttk.Button(root1, text="Select Image", command=image).pack(pady=(20,0), ipadx=50, ipady=5)
    button2 = ttk.Button(root1, text="Select Audio", command=audio).pack(ipadx=50, ipady=5)
    button3 = ttk.Button(root1, text="Change", command=job).pack(pady=(15,0), ipadx=50, ipady=5)
    button4 = ttk.Button(root1, text="Clear", command=clear).pack(pady=(5,0))

    #start program
    root1.mainloop()

def cover():

    root2= tk.Toplevel(root)
    root2.geometry('400x300')
    root2.title('Cover Art Changer')


    def soundcloud_Download():
        req = requests.get(inputValue).content.decode('utf-8')

        search = re.search(r'<meta property=\"og:image\" content=\"(.*?)\">', req).group(1)
        file_size_request = requests.get(search, stream=True)

        # Getting response of http request without content-length therefore implemented this 
        file_size = len(file_size_request.content)

        block_size = 1024 
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        with open(filename + '.jpg', 'wb') as f:
            for data in file_size_request.iter_content(block_size):
                f.write(data)
        # label1 = Label(root2, text="Image downloaded successfully")
        # label1.pack()
        box1 = messagebox.showinfo("Done","Image downloaded successfully")  


    def spotify_Download():
        req = requests.get(inputValue).content.decode('utf-8')

        search = re.search(r'Spotify is currently not available in your country', req)
        search2 = re.search(r'<meta property=\"og:image\" content=\"(.*?)\" />', req)

        list = []
        regexlist = [search, search2]
        for id,val in enumerate(regexlist):
            if val is not None:
                list.append(id)

        if 0 in list:
            print("Spotify is currently not available in your country. Please use a VPN")
        if 1 in list:
            _y = search2.group(1)
            file_size_request = requests.get(_y, stream=True)
            filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
            file_size = int(file_size_request.headers['Content-Length'])
            block_size = 1024 
            with open(filename + '.jpg', 'wb') as f:
                for data in file_size_request.iter_content(block_size):
                    f.write(data)
            # label1 = Label(root2, text="Image downloaded successfully")
            # label1.pack()
            box2 = messagebox.showinfo("Done","Image downloaded successfully")  


    def get_input():
        global inputValue
        inputValue=textBox.get("1.0","end-1c")
        spotify = re.match(r'^(https:|)[/][/]([^/]+[.])*open.spotify.com', inputValue)
        soundCloud = re.match(r'^(https:|)[/][/]([^/]+[.])*soundcloud.com', inputValue)
        if spotify:
            t = threading.Thread(target=spotify_Download)
            t.start()
        elif soundCloud:
            t = threading.Thread(target=soundcloud_Download)
            t.start()
        else:
            # label1 = Label(root2, text="Error")
            # label1.pack()
            box3 = messagebox.showerror("Error","Unknown Error!!")  

    def clean():
        textBox.delete("1.0", "end")

    textBox=Text(root2, height=5, width=30)
    textBox.pack(pady=(20,0), ipadx=50, ipady=5)
    button =ttk.Button(root2, text="Download", command=lambda: get_input())
    button.pack(pady=(20,0), ipadx=50, ipady=5)
    button2 =ttk.Button(root2, text="Clear", command=lambda: clean())
    button2.pack(pady=(20,0), ipadx=50, ipady=5)

    mainloop()

def open_browser():
    new = 1
    url = "https://github.com/sameera-madushan/CoverMaster"
    webbrowser.open(url,new=new)

root = tk.Tk()

root.geometry('300x200')
root.title('CoverMaster')

#remove the maximize button
root.resizable(0,0)

b1 = ttk.Button(root, text="Change Cover", command=changer)
b1.pack(pady=(20,0), ipadx=50, ipady=5)
b1 = ttk.Button(root, text="Download Cover", command=cover)
b1.pack(pady=(20,0), ipadx=50, ipady=5)
b1 = ttk.Button(root, text="Star This Project", command=open_browser)
b1.pack(pady=(20,0), ipadx=30, ipady=5)

root.mainloop()