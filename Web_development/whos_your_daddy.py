def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'<h1>whos your daddy</h1>']

if __name__ == '__main__':
	application()