#!/usr/bin/env python
# coding: utf-8

import tornado.ioloop
import tornado.web
from tornado.options import define, options

import os
import config

import pymongo

define("port", default=8888, help="run on the given port", type=int)
        
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
         	#these static files should better be served by nginx - here it is for dev purpose
			(r"/favicon.ico", tornado.web.StaticFileHandler, {"path": "static/favicon.ico"}),
			#(r"/robots.txt", tornado.web.StaticFileHandler, {"path": "static/robots.txt"}),
			(r"/", MainHandler),
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
 
 
 
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("main.html") 
 
 
 
def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()