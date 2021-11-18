
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Google Chrome 53 (Win 10 x64): Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&source/id'
        f'=chrome&ie=UTF-8',
        headers=headers)
    print("Подождите загружаю данные ......\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + "°C")


print("Введите название Города: ")
city = input()
city = city + " weather"
weather(city)
