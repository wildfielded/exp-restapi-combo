#!/usr/bin/python3

#####=====----- TEMPORAL for WinDev -----=====#####
import sys
sys.path.append('VENV/Lib/site-packages')
###################################################

from os import path

from fastapi import FastAPI, responses
import uvicorn


''' =====----- Global variables -----====='''

srv = FastAPI()
# Корневой index.html
ROOT_INDEX = path.join(path.dirname(path.abspath(__file__)),
                       'adds_srv/index.html')


''' =====----- Endpoints -----===== '''

@srv.get('/')
async def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы FastAPI
    Rturns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    return responses.FileResponse(ROOT_INDEX)


@srv.get('/index', response_class=responses.HTMLResponse)
async def server_index() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы FastAPI
    Rturns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    return responses.FileResponse(ROOT_INDEX)
    

''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    uvicorn.run(
        'main_fastapi:srv',
        host='0.0.0.0',
        port=8080,
        reload=True
    )

#####=====----- THE END -----=====#########################################