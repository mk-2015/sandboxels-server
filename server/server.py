import json
import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# Init

with open("config.json", "r") as file:
    cfg = json.load(file)

os.makedirs(cfg["root"], exist_ok=True)
os.makedirs(cfg["hidden"], exist_ok=True)

app.mount("/", StaticFiles(directory=cfg["root"], html=True), name="root")

host = cfg["server"]["hosts"]

if cfg["ssl"]["use ssl"]:
    port = cfg["server"]["sslport"]
    ssl_cert = cfg["ssl"]["cert"]
    ssl_key = cfg["ssl"]["key"]
else:
    port = cfg["server"]["port"]
    ssl_cert = None
    ssl_key = None

## Apis
@app.get("/api/test"):
def test()
    return "Hello this is a test!"

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host=host,
        port=port,
        ssl_certfile=ssl_cert,
        ssl_keyfile=ssl_key,
        reload=True
    )
