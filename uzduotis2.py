import requests
from bs4 import BeautifulSoup
from random import randint

url = 'http://quotes.toscrape.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

quotes = []

blocks = soup.find_all('div', class_='quote')
for block in blocks:
    quote = block.find('span', class_='text').get_text()
    author = block.find('small', class_='author').get_text()
    hint1 = ""
    splitted = author.split()
    for word in splitted:
        if '.' not in word:
            hint1 += f"{word[0]}."
        else:
            hint1 += word
    hint2_link = block.find("a", string="(about)")['href']
    quotes.append({"quote": quote, 'author': author, 'hint1': hint1, 'hint2_link': hint2_link})
#
def get_second_hint(i):
    r = requests.get(f"{url}{quotes[i]['hint2_link']}")
    soup = BeautifulSoup(r.text, 'html.parser')
    born = soup.find("div", class_="author-details").p.get_text()
    return born

print(quotes)

while True:
    i = randint(0, 9)
    print(quotes[i]['quote'])
    answer1 = input("You answer: ")
    if answer1 == quotes[i]['author']:
        print(f"Correct! Author is {quotes[i]['author']}")
    else:
        print(quotes[i]['hint1'])
        answer2 = input("You answer: ")
        if answer2 == quotes[i]['author']:
            print(f"Correct! Author is {quotes[i]['author']}")
        else:
            print(get_second_hint(i))
            answer3 = input("You answer: ")
            if answer3 == quotes[i]['author']:
                print(f"Correct! Author is {quotes[i]['author']}")
            else:
                print(f"Wrong! Author is {quotes[i]['author']}")
    if_continue = input("Continue? y/n: ")
    if if_continue != "y":
        break

