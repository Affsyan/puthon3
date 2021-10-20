"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и
выполнить обратное преобразование (используя методы encode и decode)
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for num in range(len(words)):
    words[num] = words[num].encode('utf-8')

print(words)

for num in range(len(words)):
    words[num] = words[num].decode('utf-8')

print(words)
