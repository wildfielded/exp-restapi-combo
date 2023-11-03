#!/usr/bin/python3

#####=====----- TEMPORAL for WinDev -----=====#####
import sys
sys.path.append('VENV\\Lib\\site-packages')
###################################################

# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# swagger_config_path = os.path.join(current_dir, 'swagger_conf/swagger.yaml')

from bottle import Bottle, HTTPError, request, run
# from swagger_ui import bottle_api_doc

import srv_api as api_


''' =====----- Global variables -----====='''

srv = Bottle()
# Корневой index.html
ROOT_INDEX = 'adds_srv/index.html'


''' =====----- Server resources -----===== '''

@srv.route('/', method='GET')
def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        return f_.read()


@srv.route('/index', method='GET')
def server_root() -> str:
    ''' Дубль index.html для отработки Swagger
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        return f_.read()


@srv.route('/srv/auth/login', method='POST')
def login_post() -> dict:
    ''' Аутентификация на сервере через метод POST
    '''
    return api_.login_getpost(request.json)


@srv.route('/srv/auth/login', method='GET')
def login_get() -> dict:
    ''' Аутентификация на сервере через метод GET
    '''
    return api_.login_getpost(dict(request.query))


''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    run(srv,
        host='0.0.0.0',
        port=8080,
        debug=True
       )

#####=====----- THE END -----=====#########################################