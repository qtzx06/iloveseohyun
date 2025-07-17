#!/usr/bin/env python3
"""
Simple HTTP server for testing SEOHYUN landing page
Usage: python3 server.py
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom logging with colors
        print(f"\033[92m[{self.log_date_time_string()}]\033[0m {format % args}")

def open_browser():
    """Open browser after server starts"""
    time.sleep(1)
    webbrowser.open(f'http://localhost:{PORT}')

def main():
    # Change to the directory containing the HTML files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"\n🚀 \033[94mSEOHYUN Landing Page Server\033[0m")
        print(f"📁 Serving directory: {os.getcwd()}")
        print(f"🌐 Server running at: \033[92mhttp://localhost:{PORT}\033[0m")
        print(f"📄 Access your site at: \033[92mhttp://localhost:{PORT}/index.html\033[0m")
        print(f"⚡ Press Ctrl+C to stop the server\n")
        
        # Open browser in background
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n\n🛑 \033[93mServer stopped\033[0m")
            httpd.shutdown()

if __name__ == "__main__":
    main()