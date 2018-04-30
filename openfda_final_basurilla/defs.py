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

    while a < nlimit:
        try:
            warninglist.append(repos['results'][a]["warnings"][0])
            a += 1
            try:
                druglist.append(repos['results'][a]["openfda"]["brand_name"][0])
                b += 1

        except KeyError:
            warninglist.append('Unknown')
            a += 1

    b = 0
    druglist = []

    while b < nlimit:
        try:
            druglist.append(repos['results'][a]["openfda"]["brand_name"][0])
            a += 1

        except KeyError:
            druglist.append('Unknown')
            a += 1

    with open("manufacturer_list.html", "w") as f:
        f.write('<body style="background-color:palegreen">')
        f.write("<head>" + "<h1>" + "WARNINGS LIST" + "</h1>" + "</head>")
        f.write("<ol>")

    a = 0
    while a < nlimit:
        element_1 = "<t>" + "<li>" + "warnings for" + druglist[i] + "are:" + warninglist[i]
        f.write(element_1)


    with open("manufacturer_list.html", "w"):
        self.wfile.write(bytes('<html><head><h1>Search OpenFDA Application</h1><h3>Warnings List</h3><body style="background-color: palegreen" >\n<ol>', "utf8"))

        while a < nlimit:
            try:
                for n in range(len(repos['results'][i]["openfda"]["brand_name"])):
                    try:
                        drug = "<li>"+ "brand name is: " + repos['results'][i]["openfda"]["brand_name"][0] + "</li>"
                        self.wfile.write(bytes(drug, "utf8"))
                    except KeyError:
                        break
            except KeyError:
                drug = "<li>" + "brand name is: " + "NOT FOUND" + "</li>"
                self.wfile.write(bytes(drug, "utf8"))
                continue
        self.wfile.write(bytes('</ol><h3>Thank you, come again</h3> \n <img src="http://www.konbini.com/en/files/2017/08/apu-feat.jpg" alt="Sad"><p><a href="http://%s:%s/">Back to Main Page</a></p></head></html>' % (IP, PORT), "utf8"))




elif nlimit > 100:
print("este")
print("ERROR")
with open("error.html", "r") as f:
    mensaje = f.read()
    self.wfile.write(bytes(mensaje, "utf8"))


elif nlimit > 100:
print("ERROR")
with open("error.html", "r") as f:
    mensaje = f.read()
    self.wfile.write(bytes(mensaje, "utf8"))