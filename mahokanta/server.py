# coding: utf-8
from webob.dec import wsgify
from wsgiref.simple_server import make_server


def main():

    @wsgify
    def dump(request):
        #print dir(request)
        #print dict(request.headers)
        #print request.text
        # 一番見易い出し方
        print request.as_text()

        # 最後のこれは、何も print しなくても被アクセス毎に出る
        # --------
        # 1.0.0.127.in-addr.arpa - - [27/Feb/2013 20:10:31] "GET / HTTP/1.1" 200 2
        # --------

        # ブラウザへのレスポンス
        return "OK"

    httpd = make_server('', 8080, dump)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
