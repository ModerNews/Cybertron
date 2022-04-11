from fastapi import FastAPI, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import aiofiles

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
tempalates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/file")
async def say_hello():
    with open(".\\templates\\test_template.html", "r") as content:
        return HTMLResponse(content.read())


@app.post("/uploads")
async def create_file(request: Request):
    form = await request.form()
    print(form)
    filename = form["file"].filename
    contents = await form["file"].read()
    with open(filename, 'wb') as f:
        f.write(contents)
    return filename