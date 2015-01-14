import sys

def application(environ, start_response):
    ret = start_response('200 OK', [('Content-Type', 'text/plain')])

    return ['Hello World!\nVERSION: %s\nPYTHONPATH: %s\nRET: %s' % (sys.version, sys.path, ret)]