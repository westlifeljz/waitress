def app(environ, start_response):
    path_info = environ['PATH_INFO']
    if path_info == '/no_content_length':
        headers = []
    else:
        headers = [('Content-Length', '9')]
    write = start_response('200 OK', headers)
    if path_info == '/long_body':
        write(b'abcdefghij')
    elif path_info == '/short_body':
        write(b'abcdefgh')
    else:
        write(b'abcdefghi')
    return []

if __name__ == '__main__':
    from waitress import serve
    serve(app, port=61523, verbose=False)
    
