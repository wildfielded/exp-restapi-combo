#!/usr/bin/python3

''' =====----- Global variables -----====='''

# Корневой index.html
ROOT_INDEX = 'adds_srv/index.html'

''' =====----- Server resources -----===== '''

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