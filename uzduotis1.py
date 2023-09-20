import requests
from bs4 import BeautifulSoup
from random import shuffle

html = requests.get("https://www.delfi.lt/").text
soup = BeautifulSoup(html, 'html.parser')

title_tags = soup.select('.CBarticleTitle')
print(len(title_tags))
titles = [i.get_text() for i in title_tags]
bad_words = ['COVID', 'mirt', 'NVSC', 'skiep', 'Ukrain', 'kar']

first_parts = []
second_parts = []

# counter = 0

for title in titles:
    if ":" in title:
        if not any(word in title for word in bad_words):
            # print(title)
            # counter += 1
            splitted = title.split(": ")
            first_parts.append(splitted[0])
            second_parts.append(splitted[1])

shuffle(second_parts)

for i in range(len(first_parts)):
    print(f"{first_parts[i]}: {second_parts[i]}")

# print(counter)
