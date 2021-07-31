import requests


# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.9094897242003e-5,"date":"Tue, 27 Jul 2021 11:55:01 GMT","inverseRate":14472.848790809},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.8605635751213e-5,"date":"Tue, 27 Jul 2021 11:55:01 GMT","inverseRate":17063.205392825}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
