# coding: utf-8
#

import argparse
import os
import socket
import sys
from typing import Union, Optional

import tornado.httpserver
import tornado.web
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging


def _is_port_listening(port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('localhost', port))
        return False
    except OSError:
        return True
    finally:
        s.close()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--addr", type=str, default=":5000", help="listen port [default :5000]")
    return parser.parse_args()
    

def listen_and_serve(addr: str,
                    handler: Union[tornado.web.Application, list],
                    debug: Optional[bool]=None,
                    root_dir: str = "."):
    """
    Listen and serve

    Usage example:
        listen_and_serve(":5000", [
            (r"/", MainHandler),
            (r"/simple", SimpleHandler),
        ])
    """
    host, port = addr.split(":", 1)
    port = int(port)

    if debug is None:
        debug = (os.getenv("DEBUG") == "true")

    if _is_port_listening(port):
        sys.exit("[simple_tornado] Warning, localhost:{} is already listening".format(port))

    settings = {
        'static_path': os.path.join(root_dir, 'static'),
        'template_path': os.path.join(root_dir, 'templates'),
        'debug': debug,
    }

    if isinstance(handler, list):
        handler = tornado.web.Application(handler, debug=debug)

    http_server = tornado.httpserver.HTTPServer(handler, xheaders=True)
    http_server.listen(port)

    if debug:
        enable_pretty_logging()

    if sys.platform == 'win32' and sys.version_info[:2] == (3, 8):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        print("[simple_tornado] Listening on {}".format(addr))
        IOLoop.instance().start()
    except KeyboardInterrupt:
        IOLoop.instance().stop()

