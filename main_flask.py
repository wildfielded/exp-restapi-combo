#!/usr/bin/python3

from flask import Flask

import api_srv as api_


''' =====----- Global variables -----====='''

app = Flask(__name__)
# Корневой index.html
ROOT_INDEX = 'adds_srv/index.html'


''' =====----- Server resources -----===== '''

@app.route('/')
def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        return f_.read()


@app.route('/index')
def server_root() -> str:
    ''' Дубль index.html для отработки Swagger
    Returns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        return f_.read()


@app.route('/bottle/auth/login')
def login_get() -> dict:
    ''' Аутентификация на сервере через метод GET
    '''
    return api_.login_getpost(dict(request.query))


''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
       )

#####=====----- THE END -----=====#########################################