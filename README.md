## simple_tornado
Make tornado use more simple

## Installation
```bash
pip3 install simple_tornado
```

## Usage
```python
import tornado.web
import simple_tornado


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello Index page")


if __name__ == "__main__":
	simple_tornado.listen_and_serve(":5000", [
		(r"/", MainHandler)
	])
```

## LICENSE
[MIT](LICENSE)
