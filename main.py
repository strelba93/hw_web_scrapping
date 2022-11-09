import requests

import bs4


KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Браузеры', 'Разработка игр *'}

response = requests.get('https://habr.com/ru/all/')
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="tm-article-snippet")


for article in articles:
    # hubs = article.find_all(class_="tm-article-snippet__hubs")
    # hubs = [hub.find('a').text for hub in hubs]

    # if hubs in KEYWORDS:
        date_tag_time = article.find('time')
        date = date_tag_time.attrs['title']
        article_tag_a = article.find('h2').find('a')
        article_name = article_tag_a.text
        href = article_tag_a.attrs['href']
        url = 'https://habr.com' + href
        print(f"<Date>:{date}, <Header>: {article_name}, <Link>: {url}")
        print('------------------------------------------------------------')
