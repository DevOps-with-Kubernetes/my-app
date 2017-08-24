import os
import signal
import time
import threading
from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer
)


class MyMsgHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "OK"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode())
        return

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()
        return


class MyApp(object):

    def __init__(self):
        self.httpd = HTTPServer(('0.0.0.0', 5000), MyMsgHandler)

    def run(self):
        print('running server...')
        self.httpd.serve_forever()

    def stop(self):
        print('stopping server...')
        threading.Thread(target=self.httpd.shutdown).start()

if __name__ == '__main__':
    def graceful_exit_handler(signum, frame):
        app.stop()
    app = MyApp()
    signal.signal(signal.SIGTERM, graceful_exit_handler)
    app.run()
