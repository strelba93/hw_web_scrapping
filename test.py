import requests

import bs4

response = requests.get('https://lenta.ru/parts/text')
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="card-big__title tdtk")

print(articles)

