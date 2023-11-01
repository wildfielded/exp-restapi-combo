#!/usr/bin/python3

#####=====----- TEMPORAL for WinDev -----=====#####
import sys
sys.path.append('VENV\\Lib\\site-packages')
###################################################

from fastapi import FastAPI, responses
import uvicorn


''' =====----- Global variables -----====='''

# Корневой index.html
ROOT_INDEX = 'adds_srv/index.html'
srv = FastAPI()


''' =====----- Endpoints -----===== '''

srv.get('/')
async def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы FastAPI
    Rturns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    return str(responses.FileResponse(ROOT_INDEX))
    

''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    uvicorn.run('main_fastapi:srv', port=8080, reload=True)

#####=====----- THE END -----=====#########################################