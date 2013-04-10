#!/usr/bin/env python

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

class chess_child(Resource):
    isLeaf = True;
    def render_GET(self, request):
        print request
        return "<html><body>%s</body></html>" % request.uri

class chess(Resource):
    isLeaf = False;
    def render_GET(self, request):
        print request
        return "<html><body>%s</body></html>" % request.uri
    def getChild(self, path, request):
        return chess_child(path)


resource = chess()
factory = Site(resource)
reactor.listenTCP(8088, factory)
reactor.run()
