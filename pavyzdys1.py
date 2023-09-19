from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://m.delfi.lt/").text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_="mosaic-item")
counter = 0

with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["KATEGORIJA", "ANTRAŠTĖ", "NUORODA"])

    for blokas in blokai:
        try:
            kategorija = blokas.find("span", class_='md-headline-category').get_text().strip()
            tekstas = blokas.find("span", class_='md-headline-category').find_next_sibling().get_text().strip()
            nuoroda = blokas.find("span", class_='md-headline-category').find_next_sibling()['href']
            print(kategorija)
            print(tekstas)
            print(nuoroda)
            print("------------")
            csv_writer.writerow([kategorija, tekstas, nuoroda])
            counter += 1
        except:
            ...
    print("Surasta", counter)