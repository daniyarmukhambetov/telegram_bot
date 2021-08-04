from bs4.builder import HTML
import requests
from bs4 import BeautifulSoup


def get_main():
    temp = 'https://horo.mail.ru/prediction/{}/today/'
    temp2 = 'https://horo.mail.ru/prediction/{}/tomorrow/'
    temp3 = 'https://horo.mail.ru/prediction/{}/week/'
    temp4 = 'https://horo.mail.ru/prediction/{}/month/'
    temp5 = 'https://horo.mail.ru/prediction/{}/year/'
    temp6 = 'https://horo.mail.ru/prediction/{}//'
    # print(temp)
    d = {
        'Овен':'aries',
        'Телец':'taurus',
        'Близнецы':'gemini',
        'Рак':'cancer',
        'Лев':'leo',
        'Дева':'virgo',
        'Весы':'libra',
        'Скорпион':'scorpio',
        'Стрелец':'sagittarius',
        'Козерог':'capricorn',
        'Водолей':'aquarius',
        'Рыбы':'pisces'
    }

    for item in d.items():
        # print(temp.format(item[1]))
        r = requests.get(temp.format(item[1]))
        print(r)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('p')
        pred = ''
        for e in a:
            pred += e.text
            pred += '\n'
        with open(f'{item[0]} сегодня.txt', 'w', encoding='utf-8') as f:
            f.write(pred)


        r = requests.get(temp2.format(item[1]))
        print(r)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('p')
        pred = ''
        for e in a:
            pred += e.text
            pred += '\n'
        with open(f'{item[0]} завтра.txt', 'w', encoding='utf-8') as f:
            f.write(pred)


        
        r = requests.get(temp3.format(item[1]))
        print(r)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('p')
        pred = ''
        for e in a:
            pred += e.text
            pred += '\n'
        with open(f'{item[0]} неделя.txt', 'w', encoding='utf-8') as f:
            f.write(pred)


        r = requests.get(temp4.format(item[1]))
        print(r)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('p')
        pred = ''
        for e in a:
            pred += e.text
            pred += '\n'
        with open(f'{item[0]} месяц.txt', 'w', encoding='utf-8') as f:
            f.write(pred)


        r = requests.get(temp5.format(item[1]))
        print(r)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('p')
        pred = ''
        for e in a:
            pred += e.text
            pred += '\n'
        with open(f'{item[0]} год.txt', 'w', encoding='utf-8') as f:
            f.write(pred)




if __name__ == "__main__":
    get_main()