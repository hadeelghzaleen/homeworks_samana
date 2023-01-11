import http.server
import socketserver

port=8080
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",port),Handler)as  http:
    print("serving at port ", port)
    http.serve_forever()