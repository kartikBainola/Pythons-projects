# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 05:03:05 2018

@author: Jas
"""


from noteDB import NoteDB
from Dashboard import Dashboard

 
db=NoteDB(username="root",password="")
Dashboard().initUI(db)
   