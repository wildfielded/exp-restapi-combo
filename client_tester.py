#!/usr/bin/puthon3

import json

import requests


''' =====----- Global variables -----===== '''

# IP-адрес/FQDN и порт тестируемого сервера
SRV_ADDR = '127.0.0.1:8080'


''' =====----- Functions -----===== '''

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
    creds = {'login': 'user4', 'password': 'qwerty4'}
    print(test_login_post(creds))
    # print(test_login_get(creds))

#####=====----- THE END -----=====#########################################