from main import analyse
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.responses import FileResponse

app=FastAPI()

class Data(BaseModel):
    emf:str
    volume:str

@app.post("/data")
def compute(data:Data):
    return analyse(data.emf,data.volume)
    
@app.get("/data")
def graph():
    return FileResponse("potent1.png",media_type="image/png")
