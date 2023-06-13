from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import hashlib
import toml
# import httpx
import requests

app = FastAPI()


@app.get("/", response_class = HTMLResponse)
async def  home():
    return HTMLResponse('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Another</title>
</head>
<body>
    <p>Hello!</p>
    <form action="response_to_captcha_server" method="post">
        <button type="submit" class="button" >Пройти капчу </button>
    </form>
    
</body>
</html>''')

@app.post('/response_to_captcha_server/', response_class=HTMLResponse) 
async def response_to_captcha_server():
    TOKEN = '96d5dbb402b62d37e8e39c77c110e5c9'
    r = requests.get(f'URL/captcha/API_KEY/{TOKEN}/')
    
    if r.status_code == 200:
        return HTMLResponse(r.content)
    
# @app.post('/send_answer/', response_class=HTMLResponse)
# async def send_anser

if __name__ == '__main__':
    uvicorn.run(app, port = 8001, host = '0.0.0.0')