import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-populer')
def detik_populer():
    url = requests.get('https://detik.com/terpopuler/news', params={'utm_source': 'wp detiknews'})

    soup = BeautifulSoup(url.text, 'html.parser')

    area_populer = soup.find(attrs={'class': 'grid-row list-content'})

    titles = area_populer.find_all(attrs={'class': 'media__title'})
    images = area_populer.find_all(attrs={'class': 'media__image'})

    return render_template('data-scraper.html', images=images)

@app.route('/idr-rates')
def idr_rates():
    source = json_data = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas=json_data.values())

if __name__ =='__main__':
    app.run(debug=True)