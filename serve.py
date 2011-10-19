#!/usr/bin/env python
# coding: utf-8

import tornado.ioloop
import tornado.web
from tornado.options import define, options

import os
import config

import pymongo

define("port", default=8888, help="run on the given port", type=int)
define("mongodb", default="127.0.0.1:27017", help="MongoDB")
		
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
         	#these static files should better be served by nginx - here it is for dev purpose
			(r"/favicon.ico", tornado.web.StaticFileHandler, {"path": "static/favicon.ico"}),
			#(r"/robots.txt", tornado.web.StaticFileHandler, {"path": "static/robots.txt"}),
			(r"/", MainHandler),
			(r"/route/(?P<route_id>[^\/]+)", RouteHandler),
        ]
        settings = dict(
            cookie_secret=config.COOKIE_SECRET,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            autoescape=None,
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
 
connection = pymongo.Connection(options.mongodb)
db = connection.hickingpath
 
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		routes = db.routes.find()
		routes = [{'title': r['title'], 'id' : r['_id']} for r in routes]
		self.render("main.html", routes=routes) 
 
class RouteHandler(tornado.web.RequestHandler):
 	def get(self, route_id):
 		from pymongo.objectid import ObjectId
 		route = db.routes.find_one(ObjectId(route_id))
		path = route['path']
		path.insert(0, route['origin'])
		path.append(route['destination'])
		
		self.render("route.html", 
				title=route['title'], 
				origin=route['origin'],
				destination=route['destination'],
				path=path) 
 
def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()