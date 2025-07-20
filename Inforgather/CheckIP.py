import socket
import requests
import pprint
import json

hostname = input("Enter hostname: ")
ip_address = socket.gethostbyname(hostname)

url = "https://geolocation-db.com/jsonp/" + ip_address
response = requests.get(url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
    pprint.pprint(f"{k}: {v}")

