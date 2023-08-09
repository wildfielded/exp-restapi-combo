#!/usr/bin/python3

from bottle import Bottle, HTTPError, request, run

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