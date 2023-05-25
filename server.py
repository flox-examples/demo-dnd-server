from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.error import HTTPError
from urllib.request import urlopen


PORT = 5500


class DNDRequestHandler(BaseHTTPRequestHandler):
    """Makes requests to a D&D 5th Edition API to get information about skills and spells.
    """
    def do_GET(self):
        path_components = parse_path(self.path)
        try:
            (status, api_response) = make_request(path_components)
        except HTTPError:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"That path doesn't exist!")
        else:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(api_response)



def parse_path(path):
    return path.split("/")[1:]


def make_request(components):
    url = "https://dnd5eapi.co/api"
    for c in components:
        url += f"/{c}"
    response = urlopen(url, timeout=1)
    return (response.status, response.read())


def main():
    try:
        server = HTTPServer(("0.0.0.0", PORT), DNDRequestHandler)
        print(f"Started server on port {PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        print("\nStopping the server")


if __name__ == "__main__":
    main()