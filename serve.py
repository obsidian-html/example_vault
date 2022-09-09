# Normally, you can just run python -m http.server --directory output/html
# But on Windows this gives me  "was blocked because of a disallowed MIME type (“text/plain”)" errors when loading javascript files.
# This script replace the former command and can be run like python ./serve.py

# ONLY FOR DEVELOPMENT PURPOSES!

import os
import http.server
import socketserver
PORT = 8000

os.chdir('output/html')

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
      ".js": "application/javascript",
})

httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()