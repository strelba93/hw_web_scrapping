import requests

import bs4

HEADERS = {     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'habr_web_home_feed=/all/; hl=ru; fl=ru; _ym_uid=1667930879718551342; _ym_d=1667930879; _ga=GA1.2.1235964611.1667930879; _ym_isad=2; _gid=GA1.2.2023757902.1668260588; _gat_gtag_UA_726094_1=1',
                'Host': 'habr.com',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

KEYWORDS = {'дизайн', 'фото', 'web', 'Python', 'Браузеры', 'Разработка игр', 'Читальный зал'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="tm-article-snippet")


for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = {hub.find('a').text.strip('*').strip() for hub in hubs}
    if hubs & KEYWORDS:
        date_tag_time = article.find('time')
        date = date_tag_time.attrs['title']
        article_tag_a = article.find('h2').find('a')
        article_name = article_tag_a.text
        href = article_tag_a.attrs['href']
        url = 'https://habr.com' + href
        print(f"<Date>:{date}, <Header>: {article_name}, <Link>: {url}")
        print('------------------------------------------------------------')



