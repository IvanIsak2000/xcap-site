from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

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
    
    return HTMLResponse('sign up page')


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


 
@app.post("/postdata")
def postdata(username = Form(), userage=Form()):
    return print({"name": username, "age": userage})