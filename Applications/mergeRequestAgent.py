from __future__ import annotations

import json
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


def serviceNameForRepository(repositoryName: str, branchName: str) -> str | None:
    if "BusinessAIprocessing" == repositoryName:
        if "main" == branchName:
            return "business-ai-processor"
        if "trunk" == branchName:
            return "business-ai-processor-test"
    if "BusinessAIfrontend" == repositoryName:
        if "main" == branchName:
            return "business-ai-front"
        if "trunk" == branchName:
            return "business-ai-front-test"
    if "EPlatform" == repositoryName:
        if "main" == branchName:
            return "business-ai"
        if "trunk" == branchName:
            return "business-ai-test"
    return None

def run_branch_update(body):
    try:
        params = json.loads(body)
        if "MERGED" == params['pullrequest']['state']:
            serviceName = serviceNameForRepository(params['repository']['name'],
                          params['pullrequest']['destination']['branch']['name'])
            if serviceName is not None:
                os.system('docker-compose build --no-cache ' + serviceName)
                os.system('docker-compose down')
                os.system('docker-compose up -d')
                print('Перезапущен сервис ' + serviceName)
    except Exception as e:
        print(f"Неверные значения для перезапуска сервиса {e}")

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
        content_length = int(self.headers['Content-Length'])
        self.thread = threading.Thread(target=run_branch_update,
                                       args=(self.rfile.read(content_length).decode('utf-8'),))
        self.thread.daemon = True
        self.thread.start()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 7777), MergeAgent)
    print("Script server listening on port 7777")
    server.serve_forever()
