#!/usr/bin/python3

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
swagger_config_path = os.path.join(current_dir, 'swagger_conf/swagger.yaml')

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


@app.route('bottle/auth/login', method='POST')
def login_post() -> dict:
    ''' Аутентификация на сервере
    '''
    return api_.login_post(request.json)


''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    bottle_api_doc(app,
                   config_path=swagger_config_path,
                   url_prefix='/api/doc',
                   title='Swagger docs'
                  )
    run(app,
        host='0.0.0.0',
        port=8080,
        debug=True
       )

#####=====----- THE END -----=====#########################################