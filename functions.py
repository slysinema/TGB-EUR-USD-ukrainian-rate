import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

def nbu(response): 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        string_out_web_site = soup.find('div', class_='sc-1x32wa2-9 fevpFL')

        if string_out_web_site:
            result = string_out_web_site.text[:6]
            result_with_point = result.replace(',', '.')  # Заменяем запятую на точку
            result_float = float(result_with_point)  # Преобразуем в float
            return result_float
        else:
            print('Not found.')
    else:
        print(f'Pages is not found. Error Code: {response.status_code}')

def mizhbank(response, index): 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        blocks = soup.find_all('div', class_='sc-1x32wa2-9 bKmKjX')

        # Используйте первый блок
        result= blocks[index].contents[0]   ##########Вот тут подумать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        result_with_point = result.replace(',', '.')  # Заменяем запятую на точку
        result_float = float(result_with_point)  # Преобразуем в float

        return result_float
    else:
        print(f'Pages is not found. Error Code: {response.status_code}')

def auction(response, index):
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        blocks = soup.find_all('span', class_='Typography cardHeadlineL align')

        result= blocks[index].text[:5]
        result_with_point = result.replace(',', '.')  # Заменяем запятую на точку
        result_float = float(result_with_point)  # Преобразуем в float

        return result_float