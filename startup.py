import uvicorn
from main import app

uvicorn.run(app, port=2137, host="0.0.0.0")