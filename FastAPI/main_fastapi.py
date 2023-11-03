#!/usr/bin/python3

#####=====----- TEMPORAL for WinDev -----=====#####
import sys
sys.path.append('..\\VENV\\Lib\\site-packages')
###################################################

from fastapi import FastAPI, responses
import uvicorn


''' =====----- Global variables -----====='''

# Корневой index.html
ROOT_INDEX = "index.html"
# ROOT_INDEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\adds_srv\\index.html')
srv = FastAPI()


''' =====----- Endpoints -----===== '''

srv.get('/index/', response_class=responses.HTMLResponse)
async def server_root() -> str:
    ''' Аналог index.html в ServerRoot для начальной страницы FastAPI
    Rturns:
        [str] -- содержимое HTML-файла, заданного в глобальной
            переменной ROOT_INDEX
    '''
    # return str(responses.FileResponse(ROOT_INDEX))
    # with open(ROOT_INDEX, 'r', encoding='utf-8') as f_:
        # return f_.read()
        # r = f_.read()
    r = '''<!DOCTYPE html>
    <html lang="ru">
    <head>
        <title>Root page</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>
        <h1>Тестовая страница-заглушка</h1>
        <p></p><a href="/api/doc">Автодокументация Swagger (/api/doc)</a></p>
    </body>
    </html>
    '''
    return responses.HTMLResponse(content=r, status_code=200)

    

''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    uvicorn.run(
        'main_fastapi:srv',
        host='127.0.0.1',
        port=8080,
        reload=True
    )

#####=====----- THE END -----=====#########################################