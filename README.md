## simple_tornado
Make tornado use more simple

## Installation
```bash
pip3 install simple_tornado
```

## Usage
```python
import sys
import tornado.web
import simple_tornado


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Index page")


if __name__ == "__main__":
	simple_tornado.patch_for_windows()
	# this patch includes
	# - python 3.8 set_event_loop_policy
	# - handle Ctrl-C

    simple_tornado.listen_and_serve(":5000", [
        (r"/", MainHandler)
    ])
```

Use CorsMixin

```python
class MainHandler(simple_tornado.CorsMixin, tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Index page")
```

## LICENSE
[MIT](LICENSE)
