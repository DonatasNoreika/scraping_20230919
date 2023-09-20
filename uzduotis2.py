import requests
from bs4 import BeautifulSoup
from random import randint

url = 'http://quotes.toscrape.com'
quotes = []

page_counter = 1
while True:
    r = requests.get(f"{url}/page/{page_counter}/")
    page_counter += 1
    soup = BeautifulSoup(r.text, 'html.parser')
    no_quotes_found = soup.find_all('div', class_="col-md-8")[1].next_element.get_text().strip()
    if no_quotes_found == "No quotes found!":
        break


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



def get_second_hint(i):
    r = requests.get(f"{url}{quotes[i]['hint2_link']}")
    soup = BeautifulSoup(r.text, 'html.parser')
    born = soup.find("div", class_="author-details").p.get_text()
    return born

while True:
    i = randint(0, len(quotes) - 1)
    print("Index:", i)
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

