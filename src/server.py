from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/images', StaticFiles(directory='images'), name='images')

@app.get("/", response_class=HTMLResponse)
async def  home():
    with open ('templates/home/home.html', 'r') as file:
        html_content = file.read()
        return html_content
    

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


