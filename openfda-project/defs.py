

def act_ing:
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    data = self.path.strip('/search?').split('&')
    drug = data[0].split('=')[1]
    limit = data[1].split('=')[1]
    print("client has succesfully made a request")

    url = "/drug/label.json?search=active_ingredient:" + drug + '&' + 'limit=' + limit
    print(url)
    conn.request("GET", url, None, headers)
    r1 = conn.getresponse()
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    self.wfile.write(bytes(json.dumps(repos), "utf8"))

    active = []
    a = 0

    while a < limit:
        if 'active_ingredient' in repos['results'][a]:
            a += 1
            mydrugs.append(repos['results'][a]['id'])
        else:
            a += 1
            mydrugs.append("No drug found in this index")

    with open("active_ingredient.html", "w") as f:
        f.write("<head>" + "DRUGS' ID LIST" + "</head>")
        f.write("<ol>" + "\n")
        for element in mydrugs:
            element_1 = "<t>" + "<li>" + element
            f.write(element_1)

    with open("web3.html", "r") as f:
        file = f.read()

    web_contents = file
    web_headers = "HTTP/1.1 200"
    web_headers += "\n" + "Content-Type: text/html"
    web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))
    clientsocket.send(str.encode(web_headers + "\n\n" + web_contents))
    clientsocket.close()






#if 'brand_name' in repos['results'][a]['openfda']:
                    #a += 1
                    #active.append(repos['results'][a]['openfda']['brand_name'][0])
                #else:
                    #a += 1
                    #active.append("No brand found in this index")