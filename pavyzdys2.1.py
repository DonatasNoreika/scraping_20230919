import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

# Puslapių kiekis:
paginator = soup.find('ul', class_='pagination')
arrow_right_i = paginator.find('i', class_="icon icon-arrow-right")
page_num = int(arrow_right_i.parent.parent.find_previous_sibling().get_text())
print(page_num)

for page in range(1, page_num + 1):
    print("Page:", page)
    payload = {"page": page}
    source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung', params=payload).text
    soup = BeautifulSoup(source, 'html.parser')

    blokai = soup.find_all('div', class_ = 'mobiles-product-card card card__product card--anim js-product-compare-product')

    with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
        csv_writer = csv.writer(failas)
        csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

        for blokas in blokai:
            try:
                pavadinimas = blokas.find('a', class_ = 'mobiles-product-card__title js-open-product').text.strip()
                men_kaina = blokas.find('div', class_ = 'mobiles-product-card__price-marker').text.strip()
                kaina = blokas.find_all('div', class_ = 'mobiles-product-card__price-marker')[1].text.strip()
                print(pavadinimas, men_kaina, kaina)
                csv_writer.writerow([pavadinimas, men_kaina, kaina])
            except:
                pass