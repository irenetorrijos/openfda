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

    while a < nlimit:
        try:
            warninglist.append(repos['results'][a]["warnings"][0])
            a += 1

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
        while i < nlimit:
            element_1 = "<t>" + "<li>" + element
            f.write(element_1)