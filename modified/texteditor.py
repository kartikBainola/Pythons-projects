# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 01:52:58 2018

@author: Jas
"""


from tkinter import Tk, Text, Scrollbar, Menu, messagebox, filedialog, BooleanVar, Checkbutton, Label, Entry, StringVar, Grid, Frame,PhotoImage
import os, subprocess, json, string
from tkinter import *
from tkinter.colorchooser import *
import subprocess
import io
import tkinter.font,tkinter.ttk

class Font_wm(tkinter.Toplevel):
    def __init__(self, Font=None):

        tkinter.Toplevel.__init__(self)
        self.mainfont=Font
        self.title('Font ...')

        # Variable
        self.var=tkinter.StringVar()# For Font Face
        self.var.set(self.mainfont.actual('family'))
        self.var1=tkinter.IntVar()  # for Font Size
        self.var1.set(self.mainfont.actual('size'))
        self.var2=tkinter.StringVar() # For Bold
        self.var2.set(self.mainfont.actual('weight'))
        self.var3=tkinter.StringVar() # For Italic
        self.var3.set(self.mainfont.actual('slant'))
        self.var4=tkinter.IntVar()# For Underline
        self.var4.set(self.mainfont.actual('underline'))
        self.var5=tkinter.IntVar() # For Overstrike
        self.var5.set(self.mainfont.actual('overstrike'))


        # Font Sample
        self.font_1=tkinter.font.Font()
        for i in ['family', 'weight', 'slant', 'overstrike', 'underline', 'size']:
            self.font_1[i]=self.mainfont.actual(i)

        # Function
        def checkface(event):
            try:
                self.var.set(str(self.listbox.get(self.listbox.curselection())))
                self.font_1.config(family=self.var.get(), size=self.var1.get(), weight=self.var2.get(), slant=self.var3.get(), underline=self.var4.get(), overstrike=self.var5.get())
            except:
               pass
        def checksize(event):
            try:
                self.var1.set(int(self.size.get(self.size.curselection())))
                self.font_1.config(family=self.var.get(), size=self.var1.get(), weight=self.var2.get(), slant=self.var3.get(), underline=self.var4.get(), overstrike=self.var5.get())
            except:
                pass            
        def applied():
            self.result=(self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get())
            self.mainfont['family']=self.var.get()
            self.mainfont['size']=self.var1.get()
            self.mainfont['weight']=self.var2.get()
            self.mainfont['slant']=self.var3.get()
            self.mainfont['underline']=self.var4.get()
            self.mainfont['overstrike']=self.var5.get()
        def out():
            self.result=(self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get())
            self.mainfont['family']=self.var.get()
            self.mainfont['size']=self.var1.get()
            self.mainfont['weight']=self.var2.get()
            self.mainfont['slant']=self.var3.get()
            self.mainfont['underline']=self.var4.get()
            self.mainfont['overstrike']=self.var5.get()
            self.destroy()
        def end():
            self.result=None
            self.destroy()
            
        # Main window Frame
        self.mainwindow=ttk.Frame(self)
        self.mainwindow.pack(padx=10, pady=10)
        # Main LabelFrame
        self.mainframe=ttk.Frame(self.mainwindow)
        self.mainframe.pack(side='top',ipady=30, ipadx=30,expand='no', fill='both')
        self.mainframe0=ttk.Frame(self.mainwindow)
        self.mainframe0.pack(side='top', expand='yes', fill='x', padx=10, pady=10)
        self.mainframe1=ttk.Frame(self.mainwindow)
        self.mainframe1.pack(side='top',expand='no', fill='both')
        self.mainframe2=ttk.Frame(self.mainwindow)
        self.mainframe2.pack(side='top',expand='yes', fill='x', padx=10, pady=10)
        # Frame in [  main frame]
        self.frame=ttk.LabelFrame(self.mainframe, text='Select Font Face')
        self.frame.pack(side='left', padx=10, pady=10, ipadx=20, ipady=20, expand='yes', fill='both')
        self.frame1=ttk.LabelFrame(self.mainframe, text='Select Font size')
        self.frame1.pack(side='left', padx=10, pady=10, ipadx=20, ipady=20, expand='yes', fill='both')
        ttk.Entry(self.frame, textvariable=self.var).pack(side='top', padx=5, pady=5, expand='yes', fill='x')
        self.listbox=tkinter.Listbox(self.frame, bg='gray70')
        self.listbox.pack(side='top', padx=5, pady=5, expand='yes', fill='both')
        for i in tkinter.font.families():
            self.listbox.insert(tkinter.END, i)

        # Frame in [ 0. mainframe]
        self.bold=ttk.Checkbutton(self.mainframe0, text='Bold', onvalue='bold', offvalue='normal', variable=self.var2)
        self.bold.pack(side='left',expand='yes', fill='x')
        self.italic=ttk.Checkbutton(self.mainframe0, text='Italic', onvalue='italic', offvalue='roman',variable=self.var3)
        self.italic.pack(side='left', expand='yes', fill='x')
        self.underline=ttk.Checkbutton(self.mainframe0, text='Underline',onvalue=1, offvalue=0, variable=self.var4)
        self.underline.pack(side='left', expand='yes', fill='x')
        self.overstrike=ttk.Checkbutton(self.mainframe0, text='Overstrike',onvalue=1, offvalue=0, variable=self.var5)
        self.overstrike.pack(side='left', expand='yes', fill='x')
        
        # Frame in [ 1. main frame]
        ttk.Entry(self.frame1, textvariable=self.var1).pack(side='top', padx=5, pady=5, expand='yes', fill='x')
        self.size=tkinter.Listbox(self.frame1, bg='gray70')
        self.size.pack(side='top', padx=5, pady=5, expand='yes', fill='both')
        for i in range(30):
            self.size.insert(tkinter.END, i)

        tkinter.Label(self.mainframe1, bg='white',text='''
ABCDEabcde12345
''', font=self.font_1).pack(expand='no', padx=10,pady=10)

        # Frame in [ 2. mainframe]
        ttk.Button(self.mainframe2, text='   OK   ', command=out).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
        ttk.Button(self.mainframe2, text=' Cancel ', command=end).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
        ttk.Button(self.mainframe2, text=' Apply  ', command=applied).pack(side='left', expand='yes', fill='x', padx=5, pady=5)
        
        self.listbox.bind('<<ListboxSelect>>', checkface)
        self.size.bind('<<ListboxSelect>>', checksize)

class Editor():
    def __init__(self, root):
        self.root = root        
        self.TITLE = "KartiK Editor"
        self.file_path = None
        self.set_title()
        
        frame = Frame(root)
        self.yscrollbar = Scrollbar(frame, orient="vertical")
        self.editor = Text(frame, yscrollcommand=self.yscrollbar.set)
        self.editor.pack(side="left", fill="both", expand=1)
        self.editor.config( wrap = "word", # use word wrapping
               undo = True, # Tk 8.4 
               width = 80 )        
        self.editor.focus()
        self.yscrollbar.pack(side="right", fill="y")
        self.yscrollbar.config(command=self.editor.yview)        
        frame.pack(fill="both", expand=1)

        #instead of closing the window, execute a function
        root.protocol("WM_DELETE_WINDOW", self.file_quit) 

        #create a top level menu
        self.menubar = Menu(root)
        #Menu item File
        self.filemenu = Menu(self.menubar, tearoff=0)# tearoff = 0 => can't be seperated from window
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.colormenu = Menu(self.menubar, tearoff=0)
        self.executemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", underline=1, command=self.file_new, accelerator="Ctrl+N")
        self.filemenu.add_command(label="Open...", underline=1, command=self.file_open, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", underline=1, command=self.file_save, accelerator="Ctrl+S")
        self.filemenu.add_command(label="Save As...", underline=5, command=self.file_save_as, accelerator="Ctrl+Alt+S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", underline=2, command=self.file_quit, accelerator="Alt+F4")
        self.editmenu.add_command(label="Cut", underline=0, command=self.text_cut, accelerator="Ctrl+X",state=DISABLED)
        self.editmenu.add_command(label="Copy", underline=0, command=self.text_copy, accelerator="Ctrl+c",state=DISABLED)
        self.editmenu.add_command(label="Paste", underline=0, command=self.text_paste, accelerator="Ctrl+V")
        self.editmenu.add_command(label="Select All", underline=0, command=self.text_sall, accelerator="Ctrl+A")
        self.editmenu.add_command(label="Font", underline=0, command=self.font_dialog, accelerator="Ctrl+f")
        self.colormenu.add_command(label="Background Color", underline=0, command=self.back_color, accelerator="Ctrl+bg")
        self.colormenu.add_command(label="Foreground Color", underline=0, command=self.text_color, accelerator="Ctrl+bg")
        self.executemenu.add_command(label="Run File", underline=0, command=self.run_file, accelerator="Ctrl+rf")
        self.menubar.add_cascade(label="File", underline=0, menu=self.filemenu)    
        self.menubar.add_cascade(label= "Edit", underline=0, menu=self.editmenu)
        self.menubar.add_cascade(label= "Color", underline=0, menu=self.colormenu)
        self.menubar.add_cascade(label= "Execute", underline=0, menu=self.executemenu)
        self.editor.bind("<ButtonRelease>",self.ende)
        
        # display the menu
        root.config(menu=self.menubar)
    def run_file(self,event=None):
        subprocess.run(['python',self.file_path])
        '''with io.open('a.bat','w') as f:
              f.write('python ')
              f.write(os.path.basename(self.file_path))'''
              
        
        
    def text_cut(self,event=None):
        self.text=self.editor.get(SEL_FIRST, SEL_LAST)
        self.editor.delete(SEL_FIRST, SEL_LAST)
        
    def text_copy(self,event=None):
        self.text=self.editor.get(SEL_FIRST, SEL_LAST)
        
    def text_paste(self,event=None):
        self.editor.insert(INSERT, self.text)
        
    def text_sall(self,event=None):
        self.editor.tag_add(SEL, "1.0", END)
        
    def ende(self,event=None):
        if(self.editor.get(SEL_FIRST, SEL_LAST)!=""):
            self.editmenu.entryconfigure(0,state=NORMAL)
            self.editmenu.entryconfigure(1,state=NORMAL)
        else:
            self.editmenu.entryconfigure(0,state=DISABLED)
            self.editmenu.entryconfigure(1,state=DISABLED)
       
     
        
    def back_color(self,event=None):
        color=askcolor()
        print(color)
        self.editor.config(background=color[1])
        
    def text_color(self,event=None):
        color=askcolor()
        self.editor.config(foreground=color[1])
        
    def font_dialog(self,event=None):
        font1=tkinter.font.Font()
        fo=Font_wm(Font=font1)
        self.editor.configure(font=fo.mainfont)

        
    def save_if_modified(self, event=None):
        if self.editor.edit_modified(): #modified
            response = messagebox.askyesnocancel("Save?", "This document has been modified. Do you want to save changes?") #yes = True, no = False, cancel = None
            if response: #yes/save
                result = self.file_save()
                if result == "saved": #saved
                    return True
                else: #save cancelled
                    return None
            else:
                return response #None = cancel/abort, False = no/discard
        else: #not modified
            return True
    
    def file_new(self, event=None):
        result = self.save_if_modified()
        if result != None: #None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.editor.delete(1.0, "end")
            self.editor.edit_modified(False)
            self.editor.edit_reset()
            self.file_path = None
            self.set_title()
            

    def file_open(self, event=None, filepath=None):
        result = self.save_if_modified()
        if result != None: #None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            if filepath == None:
                filepath = filedialog.askopenfilename()
            if filepath != None  and filepath != '':
                with open(filepath) as f:
                    fileContents = f.read()# Get all the text from file.           
                # Set current text to file contents
                self.editor.delete(1.0, "end")
                self.editor.insert(1.0, fileContents)
                self.editor.edit_modified(False)
                self.file_path = filepath
                self.set_title()

    def file_save(self, event=None):
        if self.file_path == None:
            result = self.file_save_as()
        else:
            result = self.file_save_as(filepath=self.file_path)
        return result

    def file_save_as(self, event=None, filepath=None):
        if filepath == None:
            filepath = filedialog.asksaveasfilename(filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*'))) #defaultextension='.txt'
        try:
            with open(filepath, 'wb') as f:
                text = self.editor.get(1.0, "end-1c")
                f.write(bytes(text, 'UTF-8'))
                self.editor.edit_modified(False)
                self.file_path = filepath
                self.set_title()
                return "saved"
        except FileNotFoundError:
            print('FileNotFoundError')
            return "cancelled"

    def file_quit(self, event=None):
        result = self.save_if_modified()
        if result != None: #None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.root.destroy() #sys.exit(0)

    def set_title(self, event=None):
        if self.file_path != None:
            title = os.path.basename(self.file_path)
        else:
            title = "Untitled"
        self.root.title(title + " - " + self.TITLE)
        
    def undo(self, event=None):
        self.editor.edit_undo()
        
    def redo(self, event=None):
        self.editor.edit_redo()   
            

    def main(self, event=None):          
        self.editor.bind("<Control-o>", self.file_open)
        self.editor.bind("<Control-O>", self.file_open)
        self.editor.bind("<Control-S>", self.file_save)
        self.editor.bind("<Control-s>", self.file_save)
        self.editor.bind("<Control-y>", self.redo)
        self.editor.bind("<Control-Y>", self.redo)
        self.editor.bind("<Control-Z>", self.undo)
        self.editor.bind("<Control-z>", self.undo)

        
root = Tk()
root.wm_state('zoomed')
editor = Editor(root)
editor.main()
root.mainloop()