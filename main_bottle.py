#!/usr/bin/python3

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'swagger_conf/swagger.yaml')

from bottle import Bottle, HTTPError, request, run
from swagger_ui import bottle_api_doc

import api_srv as api_


''' =====----- Global variables -----====='''

app = Bottle()
# Корневой index.html
ROOT_INDEX = 'adds_srv/index.html'


''' =====----- Server resources -----===== '''

@app.route('/', method='GET')
def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        return f_.read()

''' =====----- MAIN -----===== '''

#####=====----- THE END -----=====#########################################