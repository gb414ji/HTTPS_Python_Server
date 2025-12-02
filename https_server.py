import http.server
import ssl

BANNER = r"""
╔═[ SIMPLE HTTPS SERVER ]══════════════════╗
║   Serving files over TLS like a boss.    ║
╚══════════════════════════════════════════╝
"""

print(BANNER)

server_address = ('0.0.0.0', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server running on https://0.0.0.0:4443")
httpd.serve_forever()
