def list_man():

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
    druglist = []

    while a < nlimit:
        try:
            druglist.append(repos['results'][a]["openfda"]["manufacturer_name"][0])
            a += 1

        except KeyError:
            druglist.append('No brand name found in this index')
            a += 1

    with open("manufacturer_list.html", "w") as f:
        f.write('<body style="background-color:palegreen">')
        f.write("<head>" + "<h1>" + "DRUG'S LIST" + "</h1>" + "</head>")
        f.write("<ol>")
        for element in druglist:
            element_1 = "<t>" + "<li>" + element
            f.write(element_1)