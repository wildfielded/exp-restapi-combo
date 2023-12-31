#!/usr/bin/python3

import json

import requests


''' =====----- Global variables -----===== '''

# IP-адрес/FQDN и порт тестируемого сервера
SRV_ADDR = '127.0.0.1:8080'


''' =====----- Functions -----===== '''

# Проверка / и /index
def test_index(path_: str='') -> str:
    response_ = requests.get(f'http://{SRV_ADDR}' + path_)
    return response_.text


def test_login_post(credentials: dict) -> str:
    response_ = requests.post(f'http://{SRV_ADDR}/bottle/auth/login',
                              json=credentials)
    return response_.text


def test_login_get(credentials: dict) -> str:
    response_ = requests.get(f'http://{SRV_ADDR}/bottle/auth/login',
                             params=credentials)
    return response_.text

''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    #####=====----- Тест / -----=====#####
    print(test_index(''))
    #####=====----- Тест /index -----=====#####
    print(test_index('/index'))

    '''
    from os import path
    abspath = path.abspath(__file__)
    print(abspath)
    dirname = path.dirname(abspath)
    print(dirname)
    ROOT_INDEX = path.join(dirname, 'adds_srv\index.html')
    print(ROOT_INDEX)
    '''

    # Тест login
    # creds = {'login': 'user4', 'password': 'qwerty4'}
    # print(test_login_post(creds))
    # print(test_login_get(creds))

#####=====----- THE END -----=====#########################################