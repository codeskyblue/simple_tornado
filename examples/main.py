# coding: utf-8
#

import tornado.web
import simple_tornado


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")


def main():
    args = simple_tornado.parse_args()
    simple_tornado.listen_and_serve(args.addr, [
        (r"/", MainHandler)
    ])


if __name__ == "__main__":
    main()
