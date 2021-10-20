"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess

args = [['ping', '-n', '3', 'yandex.ru'], ['ping', '-n', '3', 'youtube.com']]

for elem in args:
    subproc_ping = subprocess.Popen(elem, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
