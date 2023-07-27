import requests
import bs4

try:
    req = requests.get(input("Введите ссылку на исполнителя (yandex music)\n") + "/tracks")
    soup = bs4.BeautifulSoup(req.content, "lxml")
    name = soup.find('h1', {"class": "page-artist__title typo-h1 typo-h1_big"}).text
    print(f'Топ-10 треков исполнителя: {name}\n')
    for tracks in range(1, 11):
        track = soup.find('div', {"class": 'd-track', "data-id": f'{tracks}'})
        print(tracks, " " * (2 - len(str(tracks))), track.find("div", {"class": "d-track__name"})["title"])
except requests.exceptions.MissingSchema:
    print("Где-то ошибка")
except AttributeError:
    pass
except requests.exceptions.InvalidURL:
    print("Где-то ошибка.2")
