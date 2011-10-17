#!/usr/bin/env python
# coding: utf-8


import pymongo
import datetime

connection = pymongo.Connection("127.0.0.1:27017")
db = connection.hickingpath


paths = db.paths

#remove all
paths.remove()

#insert some paths
paths.insert({
	'title': "Pointe d'Andey",
	'author' : 'nicolas',
	'insert_date' : datetime.datetime.utcnow() 
	})
paths.insert({
	'title': "Lac d'Arvoin",
	'author' : 'nicolas',
	'insert_date' : datetime.datetime.utcnow() 
	})
	
	
fetched_paths = paths.find()
for p in fetched_paths:
	print p