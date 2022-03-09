import requests

URL = "https://www.zolo.ca"
page = requests.get(URL)

print(page.text)