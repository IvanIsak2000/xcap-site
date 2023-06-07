from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import hashlib
import os 
import sys

app = FastAPI()
app.mount('/images', StaticFiles(directory='images'), name='images')

@app.get("/", response_class = HTMLResponse)
async def  home():
    with open ('templates/home.html', 'r') as file:
        home_page = file.read()
        return home_page

@app.get('/log_in/', response_class = HTMLResponse)
async def log_in():
    with open ('templates/log_in.html', 'r') as file:
        log_in_page = file.read()
        return log_in_page


@app.get("/sign_up/", response_class = HTMLResponse)
async def sign_up():
    with open ('templates/sign_up.html', 'r') as file:
        sign_up_page = file.read() 
        return sign_up_page


@app.get('/API_KEY={TOKEN}/', response_class=HTMLResponse) 
async def get_request_with_token(TOKEN):
    '''
    функия для приёма запроса с токеном
    '''
    
    fake_db  = ['123']
    
    if TOKEN in fake_db:
        return HTMLResponse('Correct API_KEY')
    
    else:
        return HTMLResponse('False')


 
@app.post("/log_in/authorization/", response_class=HTMLResponse)
def postdata(username=Form(), password=Form()):
        
    fake_db = ['96d5dbb402b62d37e8e39c77c110e5c9']
    account_hash = hashlib.md5(b'Iwan123').hexdigest()
    print(account_hash)

    if account_hash in fake_db:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="icon" href="images/logo.svg" type="image/icon type">
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xcap</title>

        <link rel="stylesheet" href="account.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
            
        </head>
        <body>

        <ul>
        <li>Username: {username}</li>
        <li>Settings: {settings}</a></li>
        <li>Your API_KEY: {API_KEY}</li>
        <li>Exit</li>
        </ul>


        </body>
        </html>

    
            '''.format( username = username, settings = settings, API_KEY = API_KEY)

if __name__ == "__main__":
    #  uvicorn.run(app, host="127.0.0.1", port=5049)
    os.system('uvicorn server:app --reload')