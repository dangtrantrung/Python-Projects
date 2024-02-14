from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from deep_translator import GoogleTranslator



# Create Tk window
root=Tk()
root.title("Google Galaxy")
root.geometry("500x630")
root.iconbitmap('logo.ico')

load =Image.open('background.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
name=Label(root,text="Translator",fg='#FFFFFF',bd=0,bg='#03152D')
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)
button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
def clear1():
    box1.delete(1.0,END)

def translate():
    input=box.get(1.0,END)
    print(input)
    t=GoogleTranslator(source='vi', target='en')
    a=t.translate(input)
    box1.insert(END,a)
clear_button=Button(button_frame,text="Clear text",font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=clear)
clear_button.place(x=150,y=310)

trans_button=Button(button_frame,text="Translate",font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=translate)
trans_button.place(x=290,y=310)

box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=20)
clear_button1=Button(button_frame,text="Clear translate text",font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=clear1)
clear_button1.place(x=180,y=560)


root.mainloop()