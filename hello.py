def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, {0}!</h1>'.format(environ['PATH_INFO'][1:]), encoding='utf-8')]

