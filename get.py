def get(file_name):
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as f:
        res = file_name
        res += '\n'
        res += f.read()
    return res