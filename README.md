
# **📄 README.md — Simple HTTPS Server**

```
╔═[ SIMPLE HTTPS SERVER ]══════════════════╗
║   Serving files over TLS like a boss.    ║
╚══════════════════════════════════════════╝
```

## 🚀 Overview

This project provides a minimal, no-nonsense HTTPS server built using Python’s native modules.
Perfect for CTF challenges, local SSL testing, red-team simulations, or rapid prototyping.

No frameworks.
No dependencies.
Just pure Python with TLS.

---

## 🔧 Features

* Full HTTPS support using TLS
* Auto-loads `cert.pem` and `key.pem`
* Serves files from the current directory
* Clean ASCII banner on launch
* Works on Windows, Linux, and macOS

---

## 📦 Requirements

You only need Python 3 installed.

To generate a quick cert/key pair:

```bash
openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes
```

---

## ▶️ Usage

Just run:

```bash
python https_server.py
```

On startup, you will see:

```
╔═[ SIMPLE HTTPS SERVER ]══════════════════╗
║   Serving files over TLS like a boss.    ║
╚══════════════════════════════════════════╝

HTTPS server running on https://0.0.0.0:4443
```

Then open your browser:

```
https://localhost:4443
```

---

## 📁 Files Served

Anything in the same directory as `https_server.py` will be served automatically.

---

## 🔒 Security Note

This server is designed for testing and educational use only.
Do **not** deploy in production without hardening.

---

# **Updated Python Script (with working banner)**

Save this as **https_server.py**:

```python
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
```

---


