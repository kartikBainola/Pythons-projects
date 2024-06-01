# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 05:23:19 2018

@author: Jas
"""

from tkinter import *
from Note import Note
from editnote import EditNote
from addnewnote import AddNewNote
import tkinter.messagebox


class Dashboard:
    def __init__(self):
        pass
    '''
    def refresh_notes(self):
        notes=self.curr_notes
        temp=[]
        for note in notes:
            try:
                temp_note=self.db.get_one_note(note.get_idt())
                temp.append(temp_note)
            except Exception as e:
                pass
        self.show_notes(temp)
    '''   
            
        
    def show_notes(self,notes):
        i=0
        self.curr_notes=notes
        self.listbox.delete(0,self.listbox.size())
        for note in notes:
            self.listbox.insert(i,str(note.get_msg()))
            if i%2==0:
                self.listbox.itemconfig(i,bg="#c4c4c4")
            i+=1
    def search_callback(self):
        if len(self.var.get())<=0:
             tkinter.messagebox.showinfo("Invalid Action","Please Enter Search Entry")
             return
        notes=self.db.search_notes(self.var.get())
        if len(notes) ==0:
              tkinter.messagebox.showinfo("Info","No match Found")
        else:
              self.show_notes(notes)
    def list_all_callback(self):
        try:
            notes=self.db.get_all_notes()
            self.show_notes(notes) 
        except Exception as e:
            print(e)
            messagebox.showinfo("Error","Could Not Fetch Notes")
    def edit_callback(self):
        try:
            EditNote().initUI(self,self.db,self.curr_notes[self.listbox.curselection()[0]])
        except Exception as e:
            pass
        
        
        
    def add_callback(self):
        AddNewNote().initUI(self,self.db)
    
        
        
        
    def initUI(self,db):
        self.db=db
        self.root = Tk()
        self.root.geometry("630x500")
        self.root.title("Note Taking App")
              
        self.add_button=Button(self.root,width=20,bg="red",fg="white",font=('helvatica',15),text="Add New Note>>",command=lambda:self.add_callback())
        self.add_button.place(x=20,y=20)
        self.list_all_btn=Button(self.root,width=20,bg="red",fg="white",text="List All Notes",font=('helvatica',15),command=lambda:self.list_all_callback())
        self.list_all_btn.place(x=290,y=20)
        self.search_label=Label(self.root,text="Search Notes",font=('helvatica',15))
        self.search_label.place(x=20,y=90)
        self.var=StringVar()
        self.search_box=Entry(self.root,width=40,textvariable=self.var,font=('helvatica',15))
        self.search_box.place(x=20,y=130)
        self.search_button=Button(self.root,bg="red",fg="white",text="Search",font=('helvatica',10),width=13,command=lambda:self.search_callback())
        self.search_button.place(x=470,y=130)
        self.note_label=Label(self.root,text="-- Notes --",font=('helvatica',15))
        self.note_label.place(x=205,y=170)

        self.listbox = Listbox(self.root,selectmode=SINGLE,width=630,font=('helvatica',15),height=12)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.listbox.yview)
        self.listbox['yscroll'] = self.scroll.set

        #self.scroll.pack(side="right", fill="y")
        self.scroll.place(x=615,y=200,height=300)
        self.list_all_callback()
           
           
        self.listbox.bind('<<ListboxSelect>>', lambda l:self.edit_callback())
        self.listbox.place(x=0,y=200)
        
        

        
        
        
        self.root.mainloop()