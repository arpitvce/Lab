from main import analyse
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel
from fastapi.responses import FileResponse

app=FastAPI()

@app.get("/")
def home(request:Request):
    return temples.TemplateResponse("index.html",{"request":request})

@app.post("/data")
def compute(request:Request,emf:str=Form(...),volume:str=Form(...)):
    result= analyse(emf,volume)
    return templates.TemplateResponse(
            "index.html",{"request":request,"result":result,"graph":"/static/graph.png"})
    
@app.get("/data")
def graph():
    return FileResponse("potent1.png",media_type="image/png")
