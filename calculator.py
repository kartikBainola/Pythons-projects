# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 22:18:56 2018

@author: Jas
"""
from tkinter import *


# Functions For Doing Functions Automatically & Easily
def iframe(parent):
    store=Frame(parent)
    store.pack(fill='both', expand="yes")
    return store

# Calculation Engine
def dialnum(text):
    if text=="C":
        if len(displayvar.get())!=0:
            value=displayvar.get()
            displayvar.set(value[:-1])

    elif text=="CE":
        displayvar.set('')

    elif text=="=":
        k=displayvar.get()
        try:
            displayvar.set(eval(k))
        except:
            displayvar.set('Error')
    else:
        displayvar.set(displayvar.get()+text)

    return 
    
def ibutton(parent,text):
    store=Button(parent, text=text,bg="powder blue",relief="raised", font=('"new walt disney font" 15 bold'),
                         width=10,height=2)
    store.pack(side='left',fill='both', expand="yes")
    store['command']=lambda: dialnum(store['text'])
    return store

# Here Creating Parent window
root=Tk(className=" My Calculator")

# Here String Variable
displayvar=StringVar() #StringVar() # Holds a string; default value ""

# Creating Display
displaywidget=Entry(iframe(root), font=('arial 55 bold'),fg="blue",
    justify="right", relief="sunken",bd=3, textvariable=displayvar ) #FLAT | RAISED |SUNKEN |GROOVE |RIDGE
displaywidget.pack(fill='both', expand="yes", side="top")

# Creating Buttons
button_data=[
    ('C'),
    (['CE']),
    ('7','8','9','(',')'),
    ('4','5','6','*','**'),
    ('1','2','3','/','%'),
    ('.','0','=','+','-')]

# Creating Dialing Pad
keypad=iframe(root)
for i in button_data:
    print(i)
    storeframe=iframe(keypad)
    storeframe.pack(fill='both', expand="yes", side="top")
    for j in i:
        ibutton(storeframe,j)

# Parent Windows Mainloop
root.mainloop()