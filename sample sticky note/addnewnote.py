# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 04:50:25 2018

@author: Jas
"""

from tkinter import *
from noteDB import NoteDB
from Note import Note
import tkinter.messagebox

class AddNewNote:
    def __init__(self):
        pass
    def add_new_callback(self):
        msg=self.text.get("1.0",'end-1c')
        if len(msg) <=0:
            messagebox.showinfo("Invalid Action","Please Enter Note..")
            return
        try:
            obj=Note(msg=msg)
            self.db.add_note(obj)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            
            messagebox.showinfo("Success","Note Saved..")
            
            
            
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Error","Failed To Save Note.Try Again")
            
            
    def cancel_callback(self):
        self.dash.root.attributes('-disabled', False)
        self.root.destroy()
    
       
    
            
    def initUI(self,dash,db):
        self.dash=dash
        self.dash.root.attributes('-disabled', True)
        self.db=db
        self.root = Tk()
        self.root.geometry("500x450")
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_callback)
        self.root.title("Create New Note")
        self.add_label=Label(self.root,text="Add New Note Below",font=('helvatica',15))
        self.add_label.place(x=170,y=15)
        self.text = Text(self.root,font=('helvatica',15),width=55,height=18)
        self.text.place(x=0,y=40)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.text['yscroll'] = self.scroll.set

        #self.scroll.pack(side="right", fill="y")
        self.scroll.place(x=485,y=40,height=330)
        self.save_button=Button(self.root,bg="red",fg="white",text="Save",command=lambda:self.add_new_callback(),font=('helvatica',15),width=13)
        self.save_button.place(x=300,y=390)
        self.cancel_button=Button(self.root,bg="red",fg="white",text="Cancel",command=lambda:self.cancel_callback(),font=('helvatica',15),width=13)
        self.cancel_button.place(x=100,y=390)
        self.root.mainloop()