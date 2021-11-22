"""
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address()
"""
import subprocess
from ipaddress import ip_address
import socket
from tabulate import tabulate


def host_ping(host_list):
    columns = ("Узел", "Доступность")
    result = []
    for _ in host_list:
        try:
            address = ip_address(_)
        except ValueError:
            address = socket.gethostbyname(_)
        reply = subprocess.run(['ping', '-n', '1', f'{address}'])
        if reply.returncode == 0:
            result.append((address, 'Узел доступен'))
        else:
            result.append((address, 'Узел недоступен'))
    print(tabulate(result, headers=columns))


host_ping(["192.168.1.1", "ya.ru", "google.com", "10.24.9.0"])
