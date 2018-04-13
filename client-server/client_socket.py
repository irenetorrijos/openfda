import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
# now connect to the web server on port 80 (the normal http port)
s.connect(("127.0.0.1 8090", 8090))
print(s)
