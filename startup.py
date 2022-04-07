import uvicorn
from main import app

uvicorn.run(app, port=2137, host="127.0.0.1")