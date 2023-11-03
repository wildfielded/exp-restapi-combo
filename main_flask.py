#!/usr/bin/python3

#####=====----- TEMPORAL for WinDev -----=====#####
import sys
sys.path.append('VENV\\Lib\\site-packages')
###################################################

from flask import Flask

import srv_api as api_


''' =====----- Global variables -----====='''

srv = Flask(__name__)
# Корневой index.html
ROOT_INDEX = 'adds_srv/index.html'


''' =====----- Server resources -----===== '''

@srv.route('/')
def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        return f_.read()


@srv.route('/index')
def server_index() -> str:
    ''' Дубль index.html для отработки Swagger
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    return server_root()


@srv.route('/srv/auth/login')
def login_get() -> dict:
    ''' Аутентификация на сервере через метод GET
    '''
    return api_.login_getpost(dict(request.query))


''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    srv.run(
        host='0.0.0.0',
        port=8080,
        debug=True
       )

#####=====----- THE END -----=====#########################################