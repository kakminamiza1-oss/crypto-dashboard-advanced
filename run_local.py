#!/usr/bin/env python3
"""Serve the dashboard on loopback and open it in the default browser."""

from __future__ import annotations

import json
import socket
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORTS = range(8080, 8091)


class DashboardHandler(BaseHTTPRequestHandler):
    server_version = "MomentumDesk/1.0"

    def do_GET(self) -> None:
        path = urlsplit(self.path).path
        if path == "/health":
            body = json.dumps({"status": "ok"}).encode("utf-8")
            content_type = "application/json; charset=utf-8"
            status = 200
        elif path in ("/", "/index.html"):
            try:
                body = (ROOT / "index.html").read_bytes()
            except OSError:
                self.send_error(500, "index.html could not be read")
                return
            content_type = "text/html; charset=utf-8"
            status = 200
        else:
            self.send_error(404, "Not found")
            return

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: object) -> None:
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


def create_server() -> ThreadingHTTPServer:
    last_error: OSError | None = None
    for port in PORTS:
        try:
            return ThreadingHTTPServer((HOST, port), DashboardHandler)
        except OSError as exc:
            last_error = exc
    raise RuntimeError(
        f"Could not bind to {HOST} on ports {PORTS.start}-{PORTS.stop - 1}. "
        "Close another local server and try again."
    ) from last_error


def main() -> None:
    server = create_server()
    url = f"http://{HOST}:{server.server_port}/"
    print(f"Momentum Desk is running at {url}")
    print("Keep this window open; press Ctrl+C to stop the server.")
    threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Momentum Desk...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
