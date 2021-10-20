"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect

words = ('сетевое программирование', 'сокет', 'декоратор')

my_file = open("test_file.txt", "w+")

for elem in words:
    my_file.write(f'{elem} \n')

my_file.close()

with open(r'test_file.txt', 'rb') as file:
    content_file = file.read()
    encoding_file = detect(content_file)['encoding']
    print(f'Кодировка файла: {encoding_file}')

with open(r'test_file.txt', 'r', encoding=encoding_file) as file:
    print(file.read())
