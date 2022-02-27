# Glückspielautomat
# 7 Die böse Hexe des Ostens
# bekommst 7 --> bekommst Geld -/- kein 7 --> bekommst nur *******!!

from tkinter import *
import random

class Glueckspiel:
    
    def __init__(self):
        self.interfazErstellen()
        
    def interfazErstellen(self):
        frame = Tk()
        frame['bg']='black'
        frame.title('DIE BÖSE HEXE DES OSTENS 🖕')
        frame.minsize(340,450)
        frame.geometry('340x450')
        frame.resizable(0, 0)
        frame.iconbitmap('hexe0.ico')
        
        # Knopf
        knopf = Button(frame, text='Spielen!',command=self.spielen,font='consola 18 bold', background='black', foreground='red')
        knopf.pack(padx = 5, pady = 15)
        
        # Bilder
        foto = PhotoImage(file=r'koehle_ohne_ende.png')
        self.gewinner = Label(frame, image=foto)
        
        # Gründen
        self.grundNummer= [StringVar() for i in range(3)]
        position = 10
        for grund in self.grundNummer:
            label = Label(frame, textvariable=grund, background='black', foreground='yellow', font='Arial 44 bold')
            label.place(x = position, y = 100, width=100, height=100)
            position += 110
        mainloop()
        
    
    def generiertZahlen(self):
        return random.randint(0,9)  
    
     
    def spielen(self):
        gibt7 = False
        for i in range(3):
            wert = self.generiertZahlen()
            self.grundNummer[i].set(wert)
            if (wert == 7):
                gibt7 = True
                
        if (gibt7):
            self.gewinner.pack(side=BOTTOM)
        else:
            self.gewinner.pack_forget()        
               
                   
spielen = Glueckspiel()