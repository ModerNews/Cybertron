from fastapi import FastAPI, UploadFile, Request, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
tempalates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/file", response_class=HTMLResponse)
async def say_hello():
    tempalates.TemplateResponse('test_template.html', {'request': Request})


@app.post("/uploads")
async def create_file(request: Request, file: UploadFile = File(...)):
    filename = file.filename
    contents = await file.read()
    print(filename, '', contents)
    with open(filename, 'wb') as f:
        f.write(contents)
    return filename