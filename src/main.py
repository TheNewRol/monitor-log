import time
import asyncio
from Monitor import Monitor
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#add cors para permitir que la pagina conecta a nuestra api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def run():
    mydata = logGenerator("hola")
    return EventSourceResponse(mydata)

async def logGenerator(request):
    yield ({"hola": "hola"})
    time.sleep(0.5)