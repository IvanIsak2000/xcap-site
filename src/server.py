from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

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


 
@app.post("/log_in/authorization")
def postdata(username=Form(), password=Form()):
    try:
        fake_db = {'Iwan':'123'}

        print({"name": username, "password": password})

    
        if fake_db[username] == password:
            return HTMLResponse('Welcome!')
        
        else :
            return HTMLResponse('False')
    except Exception as err:
        return HTMLResponse('False')   


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5049)