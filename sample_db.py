#!/usr/bin/env python
# coding: utf-8


import pymongo
import datetime

connection = pymongo.Connection("127.0.0.1", 27017)
db = connection.hickingpath


paths = db.paths

#remove all
paths.remove()

#insert some paths
path = {
	'title': 'Pointe d''Andey',
	'author' : 'nicolas',
	'tags' : ['haute-savoie', 'aravis', 'summit'],
	'insert_date' : datetime.datetime.utcnow() 
	}
paths.insert(path)
