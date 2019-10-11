#avito parser single thread v0

import requests
from bs4 import BeautifulSoup


# https://www.avito.ru/sankt-peterburg?p=1&q=преподаватель+английского
# # 19 стр

def get_html(url):
    r = requests.get(url)
    
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div',class_='pagination-pages').find_all('a',class_ = 'pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]

    return int(total_pages)

def main():
    url = 'https://www.avito.ru/sankt-peterburg?p=1&q=преподаватель+английского'
    base_url = 'https://www.avito.ru/sankt-peterburg?'
    page_part = 'p='
    query_part = '&q=преподаватель+английского'

    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages+1):
        url_gen = base_url + page_part + str(i) + query_part
        print(url_gen)
    print(total_pages)


if __name__ == "__main__":
    main()