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