import BaseHTTPServer
import mimetypes
from fixures import HOST_NAME, PORT

class SimpleHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/word.docx':
            self.send_response(200)
            self.send_header('Content-type', mimetypes.guess_type('foo.docx')[0])
            self.end_headers()
            self.wfile.write(open('/home/hugo/openxmllib/tests/in/wordprocessing1.docx').read())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Not Found!")


if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT), SimpleHandler)
    httpd.serve_forever()
