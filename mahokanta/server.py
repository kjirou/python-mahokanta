# coding: utf-8
import logging
from argparse import ArgumentParser
from wsgiref.simple_server import make_server
from .app import dump

logger = logging.getLogger(__name__)

def main():

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', 
                        type=int,
                        default=8080)
    parser.add_argument('-H', '--host', 
                        default='')
    args = parser.parse_args()

    host = args.host
    port = args.port

    httpd = make_server(host, port, dump)
    logger.info('run on {host}:{port}'.format(host=host, port=port))
    httpd.serve_forever()


if __name__ == '__main__':
    main()
