from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def home():
    home_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xcap</title>
    </head>
    <body>
        <h1>Hello!</h1>
    </body>
    </html>
    
    '''
    return HTMLResponse(content = home_html)

@app.get('/log_in/')
async def log_in():
    '''
    функция для  входа в аккаунт
    '''
    return HTMLResponse('log in page')

@app.get("/sign_up/")
async def sign_up():
    '''
    фукнция для регистрации нового аккаунта
    '''
    return HTMLResponse('sign up page')


@app.get('/API_KEY={TOKEN}/') 
async def get_request_with_token(TOKEN):
    '''
    функия для приёма запроса с токеном
    '''
    
    fake_db  = ['123']
    
    if TOKEN in fake_db:
        return HTMLResponse('Correct API_KEY')
    
    else:
        return HTMLResponse('False')


