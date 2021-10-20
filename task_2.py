"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

byte_words = (b'class', b'function', b'method')

for elem in byte_words:
    print(f'{elem} {type(elem)} длинна {len(elem)}')

