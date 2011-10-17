#!/usr/bin/env python
# coding: utf-8


import pymongo
import datetime

connection = pymongo.Connection("127.0.0.1:27017")
db = connection.hickingpath


routes = db.routes

#remove all
routes.remove()

#insert some routes
routes.insert({
	'title': "Pointe d'Andey",
	'author' : 'nicolas',
	'origin' : [46.03540697369472, 6.4238691640624666],
	'destination' : [46.04285457684193, 6.417861015869107],
	'insert_date' : datetime.datetime.utcnow() 
	})
routes.insert({
	'title': "Lac d'Arvoin",
	'author' : 'nicolas',
	'origin' : [46.03540697369472, 6.4238691640624666],
	'destination' : [46.04285457684193, 6.417861015869107],
	'insert_date' : datetime.datetime.utcnow() 
	})
	
	
fetched_routes = routes.find()
for p in fetched_routes:
	print p