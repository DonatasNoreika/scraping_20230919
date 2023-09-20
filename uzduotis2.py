import requests
from bs4 import BeautifulSoup
from random import randint

url = 'http://quotes.toscrape.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# citatos
quotes_spans = soup.select('.text')
quotes = [quote.get_text() for quote in quotes_spans]

# Autoriai
author_smalls = soup.select('.author')
authors = [author_small.get_text() for author_small in author_smalls]

# Autorių inicialai
hints1 = []
for author in authors:
    hint = ""
    splitted = author.split()
    for word in splitted:
        if '.' not in word:
            hint += f"{word[0]}."
        else:
            hint += word
    hints1.append(hint)

# Gimimo duomenys
hints_a = soup.find_all("a", string="(about)")
hints_links = [hint_a['href'] for hint_a in hints_a]

def get_second_hint(i):
    r = requests.get(f"{url}{hints_links[i]}")
    soup = BeautifulSoup(r.text, 'html.parser')
    born = soup.find("div", class_="author-details").p.get_text()
    return born

while True:
    i = randint(0, 9)
    print(quotes[i])
    answer1 = input("You answer: ")
    if answer1 == authors[i]:
        print(f"Correct! Author is {authors[i]}")
    else:
        print(hints1[i])
        answer2 = input("You answer: ")
        if answer2 == authors[i]:
            print(f"Correct! Author is {authors[i]}")
        else:
            print(get_second_hint(i))
            answer3 = input("You answer: ")
            if answer3 == authors[i]:
                print(f"Correct! Author is {authors[i]}")
            else:
                print(f"Wrong! Author is {authors[i]}")
    if_continue = input("Continue? y/n: ")
    if if_continue != "y":
        break

