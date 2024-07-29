import os
import requests
from bs4 import BeautifulSoup
import numpy as np


def parse_position_titles(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Не удалось получить страницу, код ошибки: {response.status_code}")
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    position_titles = soup.find_all('div', class_='position_title')
    titles = [div.get_text(strip=True) for div in position_titles]
    return titles

save_dir = 'words'
os.makedirs(save_dir, exist_ok=True)

for length in range(4, 11):
    url = f'https://kupidonia.ru/spisok/spisok-suschestvitelnyh-russkogo-jazyka/bukov/{length}'
    titles = parse_position_titles(url)

    file_path = os.path.join(save_dir, f"Words with len {length}.csv")
    np.savetxt(file_path, titles, delimiter=",", fmt='%s')
    print(f"Сохранено {len(titles)} слов(а) в файл {file_path}")
