
import datetime
from tkinter import EXCEPTION, PhotoImage, Toplevel, filedialog

import tkinter as tk,urllib.request,random,sys
from io import BytesIO
from PIL import Image, ImageFont, ImageTk
import PIL.ImageDraw
import scrapetube,webbrowser,os
from threading import Thread
from PIL import Image
from tkinter import filedialog

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


windw = tk.Tk()
windw.title("Youtube Video Downloaderesource_path(")
icon=PhotoImage(file=resource_path(resource_path("Untitledos.png")))
windw.iconphoto(False,icon)
windw.configure(background="white")
windw.resizable(0,0)
ac=str(random.randint(1,20))
b=str(random.randint(20,38))
def find_file():
    aaa=filedialog.askdirectory(title="Select folder to download videos")
    return aaa
def create_folder():
    ad=find_file()
    global ac
    global b
    ads=os.path.join(ad,f"Video{ac}{b}")
    os.mkdir(ads)
    return ads
def on_defe_click(event):
    """function that gets called whenever defe is clicked"""
    if defe.get() == 'Enter your search term here':
       defe.delete(0, "end") # delete all the text in the defe
       defe.insert(0, '') #Insert blank for user input
       defe.config(fg = 'black')
def on_focusout(event):
    if defe.get() == '':
        defe.insert(0, 'Enter your search term here')
        defe.config(fg = 'grey')
defe=tk.Entry(bg="white",borderwidth=0)
defe.grid(row=2,column=2,ipadx=20,ipady=10)

pic1=Image.open(resource_path("R.png"))
pic1.info.pop('background', None)
app1=ImageTk.PhotoImage(pic1.resize((20,20)))
defe.insert(0, 'Enter your search term here')
defe.bind('<FocusIn>', on_defe_click)
defe.bind('<FocusOut>', on_focusout)
defe.config(fg = 'grey')





aadg=tk.Button(windw,borderwidth=0,command=lambda:Opennewwindow(),image=app1,bg="white",height=20)
aadg.image=app1
aadg.grid(row=2,column=3)

def Opennewwindow():
    ads=create_folder()
    global defe
    global pos
    videos=scrapetube.get_search(str(defe.get()))
    global windw
    
    root=Toplevel(windw)
    root.title("Search results")
    frame = tk.Frame(root)
    frame.grid(row = 0, column = 0, sticky = "nsew")
    frame.rowconfigure(0)
    frame.columnconfigure(0)
    
    cv = tk.Canvas(
    frame, width = 470, height = 600,background="white"
    )
    cv.grid(row = 0, column = 0, sticky = "nsew")
    
    a=[]
    pos=220
    
    class ButtonFrame: 
        def __init__(self,url,pos):
            self.url=url
            self.pos=pos
        def download(self,video_title):
            if "/"in video_title:
                video_title=video_title.replace("/","∕")
            if "\"" in video_title:
                video_title=video_title.replace("\"","`")
            if "|" in video_title:
                video_title=video_title.replace("|","∣")
            downlod = f'youtube-dl -o  \"{ads}//{video_title}.mp4\" {self.url} --abort-on-error --write-sub'
            print(len(downlod),downlod)
            Thread(target=os.system,args=(downlod,)).start()
        def create_button(self,rooted,video_title):
            kal=tk.Button(rooted,text="Play video",command=lambda:webbrowser.open(f'https://www.youtube.com/watch?v={self.url}'),borderwidth=0,background="white")
            kal.grid(row = 0, column = 1)
            zemo=tk.Button(rooted,text="Download video",background="white",borderwidth = 0,command=lambda:self.download(video_title),)
            zemo.grid(row = 0, column = 2)






    def ytgen(video,a):
        i=0
    
        image_no=0
        for video in videos:
            try:
                global pos
                u = urllib.request.urlopen(video["thumbnail"]["thumbnails"][0]["url"])
                raw_data = u.read()
                u.close()

                im = Image.open(BytesIO(raw_data))
             
                
            
                image = ImageTk.PhotoImage(im.resize((470,210)))
             
                a.append(image)
            
            
            
                axty=tk.Frame(cv,background="white",height=600)
                axty1=tk.Frame(cv,background="white",height=600)
                axty2=tk.Frame(cv,background="white",height=600)
                cv.create_window(0,pos,anchor="nw",window=axty)
                tk.Label(axty, image=a[image_no]).grid(row=0,column=0)
                image_no+=1
                pos+=220
            
                cv.create_window(0,pos,anchor="nw",window=axty1)
                lab1=tk.Label(axty1, text=video["title"]["runs"][0]["text"],wraplength=470,font=("ariel",11,"bold"),bg="white")
                lab1.pack()
                pos+=40
                cv.create_window(0,pos,anchor="nw",window=axty2)
                lab2=tk.Label(axty2, text=video["title"]["accessibility"]["accessibilityData"]['label'].replace(video["title"]["runs"][0]["text"],""),wraplength=470,font=("ariel",10),bg="white",fg="grey")
                lab2.pack()
                pos+=40
                axty3=tk.Frame(cv,background="white",height=600,)
                cv.create_window(150,pos,anchor="nw",window=axty3)
                button=ButtonFrame(video['videoId'],pos)
                button.create_button(axty3,video["title"]["runs"][0]["text"])
                pos+=40

                cv.configure(scrollregion = f"0 220 0 {pos}")

            except:
                print("cola"+EXCEPTION)
                continue
    
    Thread(target=ytgen,args=(videos,a)).start()





    vscrollbar = tk.Scrollbar(
    frame, orient = "vertical", command = cv.yview)
    vscrollbar.grid(row = 0, column = 1, sticky = "ns")
    cv.config(yscrollcommand = vscrollbar.set)


    root.update()

    def _on_mousewheel(event):
        intno=int(-1*(event.delta/120))
        cv.yview_scroll(intno, "units")
    vscrollbar.grid(row=0, column=1, sticky="sn")
    root.bind_all("<MouseWheel>",_on_mousewheel)

    


    root.mainloop()
windw.mainloop()