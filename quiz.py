# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:40:00 2018

@author: Jas
"""

import threading
import time
from tkinter import *


root = Tk()
frame=Frame(root)

h=IntVar()
m=IntVar()
s=IntVar()

totalvar=IntVar()



question=["who is the inventor of python ?","What is Django ?","India's biggest problem ?","which one is the most corrupt country ?","what is make in INDIA?"]
option=["a. Guido","b. Shawn","c. Donald","d. Sam","a. MVT","b. MVC","c. CMS","d. CRM","a. Population","b. Corruption","c. Unemployment","d. All of the above","a. India","b. Greece","c. France","d. U.A.E","a. Clean banks","b. Clean natural resources","c. Make people job less","d. all of the above"]
ans=[0,0,3,0,3]

timevar=StringVar()
timevar.set("Total time is 5 minutes")
timelabel=Label(frame,textvariable=timevar,bg="blue",font=("comic sans ms", 12),fg="white").grid(row=0,sticky=W)

var=StringVar()
var.set("Time Passed : ")
timelabel2=Label(frame,textvariable=var,bg="blue",font=("comic sans ms", 12),fg="white").grid(row = 0,column=1,padx=100)

qvar=StringVar()
qabel=Label(frame,text="",textvariable=qvar,bg="blue",font=("comic sans ms", 12),fg="white").grid(row = 1, sticky=W,pady=40)

selected = IntVar()
optvar=IntVar()

r1=StringVar()
rad1 = Radiobutton(frame,text='',textvariable=r1, value=0, variable=selected,bg="grey").grid(row = 2, sticky=W,pady=10)
r2=StringVar()
rad2 = Radiobutton(frame,text='',textvariable=r2 ,value=1, variable=selected,bg="grey").grid(row = 3, sticky=W,pady=10)
r3=StringVar()
rad2 = Radiobutton(frame,text='',textvariable=r3, value=2, variable=selected,bg="grey").grid(row = 4, sticky=W,pady=10)
r4=StringVar()
rad2 = Radiobutton(frame,text='',textvariable=r4, value=3, variable=selected,bg="grey").grid(row = 5, sticky=W,pady=10)

frame.pack(side=LEFT)

def exam_start(seconds):
     
     for x in range(300):
         time.sleep(seconds)
         s.set(s.get()+1)
         qvar.set(question[m.get()])
         r1.set(option[optvar.get()])
         r2.set(option[optvar.get()+1])
         r3.set(option[optvar.get()+2])
         r4.set(option[optvar.get()+3])
         if(s.get()==59):
             if(ans[m.get()]==selected.get()):
                 totalvar.set(totalvar.get()+10)
             m.set(m.get()+1)
             optvar.set(optvar.get()+4)
             s.set(0)
             
                 
         if(m.get()==5):
            a=(totalvar.get()/50)*100
            timevar.set("You get "+str(a)+" % marks")
        
             
         var.set("Time Passed : "+str(h.get())+" : "+str(m.get())+" : "+str(s.get()))
         
             
         
         
                    
            
            
my_thread = threading.Thread(target=exam_start, args=(1,))
my_thread.start()

root.geometry("550x400")
root.title("Quiz Contest")
root.mainloop()
