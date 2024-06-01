# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 04:53:38 2018

@author: Jas
"""

from tkinter import *
from noteDB import NoteDB
from Note import Note
import tkinter.messagebox

class EditNote:
    def __init__(self):
        pass
    def update_callback(self,note):
        msg=self.text.get("1.0",'end-1c')
        if len(msg) <=0:
            messagebox.showinfo("Invalid Action","Please Enter Note..")
            return
        try:
            obj=Note(idt=note.get_idt(),msg=msg)
            self.db.update_note(obj)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            
            messagebox.showinfo("Success","Note Updated..")
            
            
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Error","Failed To Update Note.Try Again")
            
            
    def cancel_callback(self):
        self.dash.root.attributes('-disabled', False)
        self.root.destroy()
    def delete_callback(self,note):
        try:
            self.db.delete_note(note)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            
            messagebox.showinfo("Success","Note Deleted!")
            
            
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            
            messagebox.showinfo("Error","Failed To Delete Note.Try Again")
            
            
        
    
    
    def initUI(self,dash,db,note):
        self.dash=dash
        self.dash.root.attributes('-disabled', True)
        self.db=db
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_callback)
        self.root.title("Edit Note")
        self.add_label=Label(self.root,text="View\Edit Note",font=('helvatica',10))
        self.add_label.place(x=170,y=15)
        self.text = Text(self.root,font=('helvatica',10),width=55,height=18)
        self.text.insert('1.0',note.get_msg())
        self.text.place(x=20,y=40)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.text['yscroll'] = self.scroll.set

        #self.scroll.pack(side="right", fill="y")
        self.scroll.place(x=485,y=40,height=330)
        time="Created At : "+str(note.get_time())
        self.time_label=Label(self.root,text=time,font=('helvatica',10))
        self.time_label.place(x=140,y=385)
        self.save_button=Button(self.root,bg="red",fg="white",text="Update",command=lambda:self.update_callback(note),font=('helvatica',10),width=13)
        self.save_button.place(x=330,y=430)
        self.delete_button=Button(self.root,bg="red",fg="white",text="Delete",command=lambda:self.delete_callback(note),font=('helvatica',10),width=13)
        self.delete_button.place(x=180,y=430)
        self.cancel_button=Button(self.root,bg="red",fg="white",text="Cancel",command=lambda:self.cancel_callback(),font=('helvatica',10),width=13)
        self.cancel_button.place(x=40,y=430)
        self.root.mainloop()