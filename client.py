"""Программа-клиент"""

import sys
import json
import socket
import time
import logging
import datetime
import logs.client_log_config
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message
import inspect

# Инициализация клиентского логера
CLIENT_LOGGER = logging.getLogger('client')
account_name = 'Guest'


class Log:
    def __call__(self, func):
        def decorated(*args, **kwargs):
            res_func = func(*args, **kwargs)
            CLIENT_LOGGER.info(f'log: {func.__name__}({args}, {kwargs})')
            if (inspect.stack()[1][3]) == func.__name__ or (inspect.stack()[1][3]) == '<module>':
                pass
            else:
                CLIENT_LOGGER.info(f'Функция {func.__name__} была вызвана из функции {inspect.stack()[1][3]} в: '
                                   f'{datetime.datetime.now()}')
            return res_func
        return decorated


@Log()
def create_presence(name):
    """
    Функция генерирует запрос о присутствии клиента
    :param name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано сообщение для пользователя {account_name}')
    return out


@Log()
def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


@Log()
def main():
    """
    Загружаем параметы коммандной строки
    :return:
    """
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        CLIENT_LOGGER.critical('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence(account_name)
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.error('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
