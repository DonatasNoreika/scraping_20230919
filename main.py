from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
res = soup.body.next_element.next_element.next_element.next_element.get_text()
print(res)