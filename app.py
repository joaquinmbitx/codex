from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"hola mundo!"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), HelloWorldHandler)
    print("Servidor iniciado en http://127.0.0.1:8000")
    server.serve_forever()
