import http.server
import socketserver
import http.client
import json

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8000

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
            nlimit = int(limit)
            print("Searching . . .")

            url = "/drug/label.json?search=active_ingredient:" + drug + '&' + 'limit=' + limit
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            if "error" in repos:
                print("ERROR")
                with open("error.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))

            else:

                active = []
                a = 0

                while a < nlimit:
                    try:
                        active.append(repos['results'][a]["openfda"]["brand_name"][0])
                        a += 1

                    except KeyError:
                        active.append('Unknown')
                        a += 1

                with open("active_ingredient.html", "w") as f:
                    f.write('<body style="background-color:indianred">')
                    f.write("<head>" + "<h1>" + "DRUG'S BRAND NAMES" + "</h1>" + "</head>")
                    f.write("<ol>")
                    for element in active:
                        element_1 = "<t>" + "<li>" + element
                        f.write(element_1)

                with open("active_ingredient.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))


        def man_name():
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip('/search?').split('&')
            manufacturer = data[0].split('=')[1]
            limit = data[1].split('=')[1]
            nlimit = int(limit)
            print("Searching . . .")

            url = "/drug/label.json?search=openfda.manufacturer_name:" + manufacturer + '&' + 'limit=' + limit
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            if "error" in repos:
                print("ERROR")
                with open("error.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))

            else:
                manuf = []
                a = 0

                while a < nlimit:
                    try:
                        manuf.append(repos['results'][a]["openfda"]["brand_name"][0])
                        a += 1

                    except KeyError:
                        manuf.append('Unknown')
                        a += 1

                with open("manufacturer_name.html", "w") as f:
                    f.write('<body style="background-color:lavender">')
                    f.write("<head>" + "<h1>" + "DRUG'S BRAND NAMES" + "</h1>" + "</head>")
                    f.write("<ol>")
                    for element in manuf:
                        element_1 = "<t>" + "<li>" + element
                        f.write(element_1)

                with open("manufacturer_name.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))



        def list_drug():

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            limit = self.path.split("=")[1]
            print("Searching . . .")

            url = "/drug/label.json?limit=" + limit

            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)


            nlimit = int(limit)
            a = 0
            druglist = []

            if "error" in repos:
                print("ERROR")
                with open("error.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))

            else:
                while a < nlimit:
                    try:
                        druglist.append(repos['results'][a]["openfda"]["brand_name"][0])
                        a += 1

                    except KeyError:
                        druglist.append('Unknown')
                        a += 1

                with open("drug_list.html", "w") as f:
                    f.write('<body style="background-color:#E9C2B7">')
                    f.write("<head>" + "<h1>" + "DRUGS LIST" + "</h1>" + "</head>")
                    f.write("<ol>")
                    for element in druglist:
                        element_1 = "<t>" + "<li>" + element
                        f.write(element_1)

                with open("drug_list.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))


        def list_man():

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            limit = self.path.split("=")[1]
            print("Searching . . .")

            url = "/drug/label.json?limit=" + limit
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            nlimit = int(limit)
            a = 0
            druglist = []

            if "error" in repos:
                print("ERROR")
                with open("error.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))

            else:
                while a < nlimit:
                    try:
                        druglist.append(repos['results'][a]["openfda"]["manufacturer_name"][0])
                        a += 1

                    except KeyError:
                        druglist.append('Unknown')
                        a += 1

                with open("manufacturer_list.html", "w") as f:
                    f.write('<body style="background-color:#FFFFCC">')
                    f.write("<head>" + "<h1>" + "MANUFACTURERS LIST" + "</h1>" + "</head>")
                    f.write("<ol>")
                    for element in druglist:
                        element_1 = "<t>" + "<li>" + element
                        f.write(element_1)

                with open("manufacturer_list.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))

        def list_warn():

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            data = self.path.strip('/search?').split('?')
            limit = data[1].split('=')[1]
            print("Searching . . .")

            url = "/drug/label.json?limit=" + limit
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            nlimit = int(limit)
            a = 0
            warninglist = []
            b = 0
            druglist = []

            if "error" in repos:
                print("ERROR")
                with open("error.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))

            else:

                while a < nlimit:
                    try:
                        warninglist.append(repos['results'][a]["warnings"][0])
                        a += 1

                    except KeyError:
                        warninglist.append('Unknown')
                        a += 1

                while b < nlimit:
                    try:
                        druglist.append(repos['results'][b]["openfda"]["brand_name"][0])
                        b += 1

                    except KeyError:
                        druglist.append('Unknown')
                        b += 1

                with open("manufacturer_list.html", "w") as f:
                    f.write('<body style="background-color:palegreen">')
                    f.write("<head>" + "<h1>" + "WARNINGS LIST" + "</h1>" + "</head>")
                    f.write("<ol>")

                    i = 0
                    while i < nlimit:
                        element_1 = "<t>" + "<li>" + "Warnings for " + druglist[i] + " are:" + "\n" + warninglist[i]
                        f.write(element_1)
                        i += 1

                with open("manufacturer_list.html", "r") as f:
                    mensaje = f.read()
                    self.wfile.write(bytes(mensaje, "utf8"))


        path = self.path
        print(path)


        if path == "/":
            print("SEARCH: client entered search web")
            with open("search.html",'r') as f:
                mensaje= f.read()
                self.wfile.write(bytes(mensaje, "utf8"))

        elif 'search_active_ingredient' in path:
            print('Active ingredient')
            act_ing()

        elif 'search_manufacturer' in path:
            print('Manufacturer name')
            man_name()

        elif 'search_drug' in path:
            print('Drug list')
            list_drug()

        elif 'search_manlist' in path:
            print('Company list')
            list_man()

        elif 'search_warnlist' in path:
            print('Warnings list')
            list_warn()

        else:
            print("ERROR")
            with open("error.html", "r") as f:
                mensaje = f.read()
                self.wfile.write(bytes(mensaje, "utf8"))

        return






# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("sconnected to", IP, PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("Server stopped!")