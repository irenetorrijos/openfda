import http.server
import socketserver
import http.client
import json

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8002

socketserver.TCPServer.allow_reuse_address = True
# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


        #def file_sent(nombre_arch):
         #   with open(nombre_arch,'r') as f:
             #   mensaje= f.read()



        #path = self.path

        if self.path == "/":
            print("SEARCH: client entered search web")
            with open("search4.html",'r') as f:
                mensaje= f.read()
                self.wfile.write(bytes(mensaje, "utf8"))

        elif 'search' in self.path:  #find a drug and limit that has been entered
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip('/search?').split('&')
            drug = data[0].split('=')[1]
            limit = data[1].split('=')[1]
            print("client has succesfully made a request")


            url = "/drug/label.json?search=active_ingredient:"+ drug + '&' + 'limit=' + limit
            print(url)
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)
            self.wfile.write(bytes(json.dumps(repos), "utf8"))
        return






# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Server stopped!")