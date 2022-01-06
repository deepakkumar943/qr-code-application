import socket
host="www.google.com"
try:
    ipAddr=socket.gethostbyname(host)
    print('IP address is = '+ipAddr)
except socket.gaierror:
    print("the website is not exist")
