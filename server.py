from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import os

port = 9000

data_file = open(os.environ["RESUME_PATH"], "r+")
data = json.load(data_file)


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(data))


def run(port=port):
    server_address = ("", port)
    httpd = HTTPServer(server_address, Server)

    print("Starting httpd on port: {}".format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
