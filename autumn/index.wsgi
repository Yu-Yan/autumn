import sae, os
from mysite import wsgi

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello, world!']


os.environ['DJANGO_SETTINGS_MODULE'] = 'autumn.settings'
application = sae.create_wsgi_app(wsgi.application)