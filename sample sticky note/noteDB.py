# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 04:08:36 2018

@author: Jas
"""

#import mysql.connector as mysql
import pymysql as mysql
from Note import Note

class NoteDB:
    db=None
    cursor=None
    def __init__(self,username="",password=""):
        try:
            self.db=mysql.connect(host="127.0.0.1",user=username,passwd=password,db="test")
            self.cursor=self.db.cursor()
        except Exception as e:
            raise
    def add_note(self,note):
        q="insert into note(msg) values('%s')"%(note.get_msg())
        try:
            self.cursor.execute(q)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
            raise
    def get_one_note(self,idt):
        q="select * from note where id=%d"%(idt)
        try:
            self.cursor.execute(q)
            result=self.cursor.fetchall()
            obj=Note(idt=result[0],msg=result[1],time=result[2])
            return obj
        except Exception as e:
            raise
    def get_all_notes(self):
        q="select * from note order by time desc;"
        try:
            self.cursor.execute(q)
            notes=[]
            results=self.cursor.fetchall()
            for result in results:
                obj=Note(idt=result[0],time=result[1],msg=result[2])
                notes.append(obj)
            return notes
        except Exception as e:
            raise
    def update_note(self,note):
        q="update note set msg='%s' where id=%d"%(note.get_msg(),note.get_idt())
        try:
            self.cursor.execute(q)
            self.db.commit()
        except Exception as e:
            
            self.db.rollback()
            raise
    def search_notes(self,query):
        q="select * from note where msg like '%{0}%' order by time desc".format(query)
        try:
            self.cursor.execute(q)
            notes=[]
            results=self.cursor.fetchall()
            for result in results:
                obj=Note(idt=result[0],msg=result[2],time=result[1])
                notes.append(obj)
            return notes
        except Exception as e:
            raise
    def delete_note(self,note):
        q="delete from note where id=%d"%(note.get_idt())
        try:
            self.cursor.execute(q)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise