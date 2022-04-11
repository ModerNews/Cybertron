from fastapi import FastAPI, UploadFile, Request, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import platform
import pymysql as mysql

from crud import *

class Server(FastAPI):
    def __init__(self):
        super().__init__()
        if 'linux' not in platform.system().lower():
            from sshtunnel import SSHTunnelForwarder
            self._tunnel = SSHTunnelForwarder(("192.168.137.242", 22), ssh_username="mashu",
                                              ssh_password="78632145",
                                              remote_bind_address=("localhost", 3306))
            # Cannot close tunnel after creating pymysql connection (closing it will result in crashing db connection)
            self._tunnel.start()
            self.mydb = mysql.connect(host="localhost",
                                      user="mashu",
                                      password="78632145",
                                      port=self._tunnel.local_bind_port,
                                      db="Translations",
                                      charset='utf8mb4')
        else:
            self.mydb = mysql.connect(host="localhost",
                                      user="mashu",
                                      password="78632145",
                                      db="Translations",
                                      charset='utf8mb4')



app = Server()
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get("/anime")
async def anime_view(request: Request, title: Optional[str] = None):
    episodes = get_episodes(app.mydb, title)
    return templates.TemplateResponse('anime_list.html', {'request': request, 'episodes': episodes})


@app.get("/file", response_class=HTMLResponse)
async def say_hello(request: Request):
    # print(templates.)
    return templates.TemplateResponse('file_upload.html', {'request': request})


@app.post("/uploads")
async def create_file(request: Request, file: UploadFile = File(...)):
    filename = file.filename
    contents = await file.read()
    print(filename, '', contents)
    with open(filename, 'wb') as f:
        f.write(contents)
    return filename