from collections import deque
import re
import requests
from bs4 import BeautifulSoup
import urllib.parse

userUrl = input("Enter URL: ")
if not userUrl.startswith(('http://', 'https://')):
    userUrl = 'http://' + userUrl

urls = deque([userUrl])
scraped_urls = set()
emails = set()
count = 0

try:
    while urls:
        count += 1
        if count > 20:
            break

        url = urls.popleft()
        scraped_urls.add(url)
        print("Crawling URL:", url)

        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, 'html.parser')

        for anchor in soup.find_all("a"):
            link = anchor.get("href", "")
            if link.startswith('mailto:') or link.startswith('javascript:') or link == "#":
                continue
            full_link = urllib.parse.urljoin(url, link)
            if full_link not in urls and full_link not in scraped_urls:
                urls.append(full_link)

except KeyboardInterrupt:
    print("User stopped the program.")

if emails:
    print("\nFound emails:")
    for mail in emails:
        print(mail)
else:
    print("\nNo emails found.")
