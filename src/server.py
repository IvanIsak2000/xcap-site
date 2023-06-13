from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import hashlib
import toml

app = FastAPI()
app.mount('/images', StaticFiles(directory='images'), name='images')
app.mount('/templates', StaticFiles(directory='templates'), name='templates')

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



@app.get('/captcha/API_KEY/{TOKEN}/', response_class=HTMLResponse) 
async def get_request_with_token(TOKEN):
    print(f'The site with token {TOKEN} wait captcha')
    data = toml.load("config.toml")
    ''' рандомная капча'''
    return HTMLResponse('THIS CAPTCHA')


 
@app.post("/log_in/authorization/", response_class=HTMLResponse)
async def authorization(username=Form(), password=Form()):
    fake_db = {
        '' :{
            'username':'Iwan',
            'settings': 'Empty',
            'API_KEY' : '123'}
    }
    hashed_account_data = hashlib.md5(bytes(username + password, encoding='utf-8')).hexdigest()
    if hashed_account_data in fake_db:
        account_data=fake_db[hashed_account_data]

        return f'''
        <!DOCTYPE html>
        <html>
            <head>
                <link rel="icon" href="images/logo.svg" type="image/icon type">
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>xcap</title>
                <link rel="stylesheet" href="templates/account.css">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
            </head>
            <body>
                <ul>
                    <li>Username: {account_data['username']}</li>
                    <li>Settings: {account_data['settings']}</a></li>
                    <li>Exit</li>
                </ul>
            
            <div>
                <p>Your API_KEY: {account_data['API_KEY']}</p>
            </div>
    
            </body>
         </html>'''
    else:
        return 'False'


if __name__ == '__main__':
    uvicorn.run(app, port = 8000, host = '0.0.0.0')
