"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

words = ('attribute', 'класс', 'функция', 'type')

for elem in words:
    try:
        print(bytes(elem, 'ascii'))
    except UnicodeEncodeError:
        print(f'ошибка перевода слова >{elem}< в байты')
