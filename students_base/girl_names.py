import requests
import json
from bs4 import BeautifulSoup

url = "https://ismlar.com/uz/most-searched/girl"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

names = []

ul_tag = soup.find("ul", class_="list-none text-pink-500")
for a_tag in ul_tag.find_all("a"):
    name = a_tag.text.strip()
    if name:
        names.append(name)

with open("girls_names.json", "w", encoding="utf-8") as f:
    json.dump(names, f, indent = 6, ensure_ascii=False)
