from moviepy.editor import *
import tkinter as tk
import webbrowser
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createdWidgets():

    img_label =  Label(root ,image=img)
    img_label.grid(row=1, column=1, pady=5, padx=5)

    empty_label = Label(root, text="", bg="#9E9E9E")
    empty_label.grid(row=2, column=1, pady=5, padx=5)
    empty_label2 = Label(root, text="", bg="#9E9E9E")
    empty_label2.grid(row=3, column=1, pady=5, padx=5)   
    empty_label3 = Label(root, text="", bg="#9E9E9E")
    empty_label3.grid(row=4, column=1, pady=5, padx=5)   
    empty_label4 = Label(root, text="", bg="#9E9E9E")
    empty_label4.grid(row=6, column=1, pady=5, padx=5) 
    
    youtube_label = Label(root, text="Entrer votre recherche de video/music :", bg="#EEE8AA")
    youtube_label.grid(row=5, column=0, pady=5, padx=5)

    root.youtube_text = Entry(root, width=60, textvariable=lien_link)
    root.youtube_text.grid(row=5, column=1, pady=5, padx=5)

    root.youtube_link = Button(root, text="Recherché", command=youtube_open, width=10, bg="#FF8C00")
    root.youtube_link.grid(row=5, column=2, pady=1, padx=1)

    link_label = Label(root, text="Youtube URL copier sur votre recherche :", bg="#EEE8AA")
    link_label.grid(row=8, column=0, pady=5, padx=5)

    link_label_com = Label(root, text="| Choisir le lien de votre video/music a copier en-bas |", bg="#EEE8AA")
    link_label_com.grid(row=7, column=1, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=8, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination de la video/music :", bg="#EEE8AA")
    destination_label.grid(row=9, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=60, textvariable=download_path)
    root.destination_text.grid(row=9, column=1, pady=5, padx=5)

    browe_but = Button(root, text="Choisir la destination du fichier", command=browse, width=25, bg="#FF8C00")
    browe_but.grid(row=9, column=2, pady=1, padx=1)

    download_but = Button(root, text="Telecharger la Video en mp4", command=download_video, width=25, bg="#6495ED")
    download_but.grid(row=10, column=1 , pady= 3, padx=3)

    download_audio_but = Button(root, text="Telecharger uniquement la music (mp3)", command=download_audio, width=30, bg="#6495ED")
    download_audio_but.grid(row=11, column=1 , pady= 3, padx=3)

def browse():

    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")

    download_path.set(download_dir)

def download_audio():
    url_audio = video_link.get()
    folder_audio= download_path.get()
    get_video_audio = YouTube(url_audio)
    get_audio = get_video_audio.streams.get_audio_only()
    get_audio.download(folder_audio)
    
    messagebox.showinfo("Sucess!", "Download Sucessful! You will find your audio at\n"+ folder_audio )

def download_video():

    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.filter(progressive=True, file_extension='mp4')
    get_stream.get_highest_resolution().download(folder)

    messagebox.showinfo("Sucess!", "Download Sucessful! You will find your video at\n"+ folder )
    
def youtube_open():
     
    query_label = lien_link.get()
    query_path= "https://www.youtube.com/results?search_query=" + query_label
    webbrowser.open(query_path,new=1)

root = tk.Tk()

root.geometry("940x580")
root.resizable(False, False)
root.title("Telechargeur/convertisseur youtube vers mp3/mp4")
root.config(background="#9E9E9E")

img = PhotoImage(file='images/youtube-logo-22.png')
out_file=""
lien_link = StringVar()
video_link = StringVar()
download_path = StringVar()

createdWidgets()

root.mainloop()