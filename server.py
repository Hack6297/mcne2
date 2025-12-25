from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = int(os.environ.get('PORT', 10000))

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_GET(self):
        # Redirect root to vanilla.html
        if self.path == '/' or self.path == '':
            self.path = '/vanilla.html'
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), MyHTTPRequestHandler)
    print(f'🎮 Minecraft Nesa Explorer 5 Edition')
    print(f'🌐 Server running on http://0.0.0.0:{PORT}')
    print(f'⛏️ Ready to play!')
    server.serve_forever()
