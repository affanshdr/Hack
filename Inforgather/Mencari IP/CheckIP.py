import socket
import requests
import pprint
import json

def Intro(Judul):
    print(("+")+("-"*(len(Judul)+2))+("+"))
    print(f"| {Judul} |")
    print(("+")+("-"*(len(Judul)+2))+("+"))

Intro("Check IP")

print("Contoh Hostname : google.com")
hostname = input("Input Hostname  : ")
ip_address = socket.gethostbyname(hostname)

url = "https://geolocation-db.com/jsonp/" + ip_address
print("\n")
print(f"Info Hostname dari {hostname}")
response = requests.get(url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
    pprint.pprint(f"{k}: {v}")

print("\n")