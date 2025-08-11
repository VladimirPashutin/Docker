from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import threading
import os

def run_branch_update(arg):
    os.system('echo ' + str(arg))

class MergeAgent(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, srv):
        self.thread = None
        super().__init__(request, client_address, srv)

    def do_GET(self):
        self._handle_request()

    def do_POST(self):
        self._handle_request()

    def _handle_request(self):
        if self.thread is not None:
            self.thread.join()
        url = urlparse(self.path)
        if url.path is None:
            return
        if url.path.startswith("/"):
            url = url.path[1:]
        else:
            url = url.path
        self.thread = threading.Thread(target=run_branch_update, args=(url,))
        self.thread.daemon = True
        self.thread.start()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 7777), MergeAgent)
    print("Script server listening on port 7777")
    server.serve_forever()
