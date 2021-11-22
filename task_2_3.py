"""
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
from ipaddress import IPv4Address
from subprocess import Popen, PIPE
from tabulate import tabulate


def host_range_ping(ip1, ip2):
    ip_list = []
    ip1 = int(IPv4Address(ip1))
    ip2 = int(IPv4Address(ip2))
    for ip in range(ip1, ip2 + 1):
        ip_list.append(str(IPv4Address(ip)))
    return ip_list


ip_range = host_range_ping("192.168.0.1", "192.168.0.50")

"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. 
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате 
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
"""


def host_range_ping_tab(ip_list):
    ip_availability = [["Ip адресс", "Доступность"]]
    for _ in ip_list:
        proc = Popen(f"ping {_}, -w 500 -n 1", shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            ip_availability.append([_, "Доступен"])
        else:
            ip_availability.append([_, "Недоступен"])

    print(tabulate(ip_availability, headers='firstrow', tablefmt="pipe"))


host_range_ping_tab(ip_range)
