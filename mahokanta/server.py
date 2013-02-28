# coding: utf-8
from optparse import OptionParser
from webob import Response
from webob.dec import wsgify
from wsgiref.simple_server import make_server


def main():

    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port', type='int', action='store', default=8080)
    opts, args = parser.parse_args()

    @wsgify
    def dump(request):

        text = request.as_text()

        # To console
        print('--------')
        print(text)
        print('--------')

        # To browser
        return Response(text, content_type='text/plain')

    httpd = make_server('', opts.port, dump)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
