import requests
from bs4 import BeautifulSoup

url = requests.get('https://detik.com/terpopuler/news', params={'utm_source': 'wp detiknews'})

soup = BeautifulSoup(url.text, 'html.parser')

area_populer = soup.find(attrs={'class': 'grid-row list-content'})

titles = area_populer.find_all(attrs={'class': 'media__title'})
images = area_populer.find_all(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])

# print(titles)