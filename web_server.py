# Import necessary modules from the Python standard library.
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define a custom request handler class that inherits from BaseHTTPRequestHandler.
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Define a method to handle GET requests.
    def do_GET(self):
        # Send a 200 OK response status code.
        self.send_response(200)
        # Set the response header to indicate content type as HTML.
        self.send_header('Content-type', 'text/html')
        # End the response headers section.
        self.end_headers()

        # Read and serve the content of the "index.html" file.
        with open("website/index.html", "rb") as f:
            # Write the content of the file to the response output stream.
            self.wfile.write(f.read())

# Create an instance of the HTTPServer class, specifying the IP address ('0.0.0.0') and port (80) to bind to,
# and provide the custom request handler class to handle incoming requests.
httpd = HTTPServer(('0.0.0.0', 80), SimpleHTTPRequestHandler)

# Start serving the HTTP requests indefinitely using the serve_forever() method.
httpd.serve_forever()
