#!/usr/bin/python3

#####=====----- TEMPORAL for WinDev -----=====#####
import sys
sys.path.append('VENV\\Lib\\site-packages')
###################################################

import os

from fastapi import FastAPI, responses
import uvicorn


''' =====----- Global variables -----====='''

# Корневой index.html
# ROOT_INDEX = "srv_adds/index.html"
ROOT_INDEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'adds_srv/index.html')
srv = FastAPI()


''' =====----- Endpoints -----===== '''

srv.get('/index')
async def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы FastAPI
    Rturns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    return str(responses.FileResponse(ROOT_INDEX))
    

''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    uvicorn.run('main_fastapi:srv', host='127.0.0.1', port=8080, reload=True)

#####=====----- THE END -----=====#########################################