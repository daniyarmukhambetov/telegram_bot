

def do(zodiak):
    d1 = {
    'овен':u"\u2648\uFE0F",
    'телец':u"\u2649\uFE0F",
    'близнецы':u"\u264A\uFE0F",
    'рак':u"\u264B\uFE0F",
    'лев':u'\u264C\uFE0F',
    'дева':u"\u264D\uFE0F",
    'весы':u"\u264E\uFE0F",
    'скорпион':u"\u264F\uFE0F",
    'стрелец':u"\u2650\uFE0F",
    'козерог':u"\u2651\uFE0F",
    'водолей':u"\u2652\uFE0F",
    'рыбы':u"\u2653\uFE0F"
    }
    file_name = zodiak + '.txt'
    res = ''
    z, dd = zodiak.split()
    res += f'{zodiak.upper()}' 
    res += f' {d1[z.lower()]}'
    res += '\n'
    
    with open(file_name, 'r', encoding='utf-8') as f:
        res += f.read()
    return res


if __name__ == '__main__':
    print(do('Рыбы сегодня'))
