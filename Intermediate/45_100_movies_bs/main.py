import requests

from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

films = [film.getText() for film in soup.find_all(name='h3', class_='title')]
normal = list(reversed(films))

with open('100_movies.txt', 'w', encoding='utf-8') as file:
    for film in normal:
        file.write(film + '\n')