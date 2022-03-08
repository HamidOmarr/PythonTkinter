from distutils.cmd import Command
import tkinter as tk
from turtle import bgcolor

window = tk.Tk()

def ButtonOn():
    if(button['text']=='Light Switch Off'):
        button['text']='Light Switch On'
        window['background']='yellow'
        print('Aan')


    else:
        button['text']=('Light Switch Off')
        window['background']='black'
        print('Uit')
        
button = tk.Button(text='Light Switch Off', background='black', foreground='white',command=ButtonOn)
button.pack(pady = 20, padx = 20)


window.mainloop()