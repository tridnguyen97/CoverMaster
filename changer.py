'''please note: this is a very noobish script that i wrote to change the cover art of an mp3 file. 
This is my first script where i used python GUI programming. Suggestion and Criticisms are warmly welcome'''

import tkinter as tk
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
from tkinter import filedialog
from mutagen.id3 import ID3, APIC, error

#create window object
root = tk.Tk()

#remove the maximize button
root.resizable(0,0)

#title, window resolution of the main window
root.geometry('300x150')
root.title('Cover Art Changer')

# get cover image location 
def image():
    global x
    x = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("jpeg files","*.jpg")])
    if x:
        global label1
        label1 = ttk.Label(text="Image file loaded successfully").grid(row=1, column=1, padx=4, pady=4, sticky='ew')
        # label1.pack(pady=(10,0))

# get MP3 file location      
def audio():
    global y
    y = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("mp3 files","*.mp3")])
    if y:
        global label2
        label2 = ttk.Label(text="Audio file loaded successfully").grid(row=2, column=1, padx=4, pady=4, sticky='ew')

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
    label3 = ttk.Label(text="Cover art changed successfully").grid(row=3, column=1, padx=4, pady=4, sticky='ew')

# function of the clear button [button4]
def clear():
    label1 = ttk.Label(text="").grid(row=1, column=1, padx=4, pady=4, sticky='ew')
    label2 = ttk.Label(text="").grid(row=2, column=1, padx=4, pady=4, sticky='ew')
    label3 = ttk.Label(text="").grid(row=3, column=1, padx=4, pady=4, sticky='ew')
    button1 = ttk.Button(root, text="Select Image", command=image).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
    button2 = ttk.Button(root, text="Select Audio", command=audio).grid(row=2, column=0, padx=4, pady=4, sticky='ew')
    button3 = ttk.Button(root, text="Change", command=job).grid(row=3, column=0, padx=4, pady=4, sticky='ew')

button1 = ttk.Button(root, text="Select Image", command=image).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
button2 = ttk.Button(root, text="Select Audio", command=audio).grid(row=2, column=0, padx=4, pady=4, sticky='ew')
button3 = ttk.Button(root, text="Change", command=job).grid(row=3, column=0, padx=4, pady=4, sticky='ew')
button4 = ttk.Button(root, text="Clear", command=clear).grid(row=4, column=0, padx=4, pady=4, sticky='ew')


#start program
root.mainloop()