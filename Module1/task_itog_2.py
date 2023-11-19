import requests
import bs4

headers = ("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/89.0.4389.82 Safari/537.36")
url = 'https://pogoda.mail.ru/prognoz/tyumen//'
response = requests.get(url, params=headers)
soup = bs4.BeautifulSoup(response.content, 'html.parser')


def get_weather():
    item = soup.text.replace('  ', '').replace('\n', '').split('Прогноз погоды на:')[0].split('\t')
    weather_info = soup.find(class_='information__content__temperature').text
    print(f'Погода: {weather_info.strip()}', item[17])


get_weather()