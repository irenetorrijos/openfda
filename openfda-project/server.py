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

        def act_ing():
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip('/search?').split('&')
            drug = data[0].split('=')[1]
            limit = data[1].split('=')[1]
            print("Searching . . .")

            url = "/drug/label.json?search=active_ingredient:" + drug + '&' + 'limit=' + limit
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            active = []
            a = 0
            nlimit = int(limit)

            while a < nlimit:
                try:
                    active.append(repos['results'][a]["openfda"]["brand_name"][0])
                    a += 1

                except KeyError:
                    active.append('No brand name found in this index')
                    a += 1

            with open("active_ingredient.html", "w") as f:
                f.write('<body style="background-color:indianred">')
                f.write("<head>" + "<h1>" + "DRUG'S BRAND NAMES" + "</h1>" + "</head>")
                f.write("<ol>")
                for element in active:
                    element_1 = "<t>" + "<li>" + element
                    f.write(element_1)





        path = self.path

        if self.path == "/":
            print("SEARCH: client entered search web")
            with open("search.html",'r') as f:
                mensaje= f.read()
                self.wfile.write(bytes(mensaje, "utf8"))

        elif 'search_active_ingredient' in self.path:
            print('Active ingredient')
            act_ing()
            with open("active_ingredient.html", "r") as f:
                mensaje = f.read()
                self.wfile.write(bytes(mensaje, "utf8"))



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