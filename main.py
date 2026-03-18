import json


from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse

from authentication import check_creds


#import analysis
from typing import Annotated
from datamodel import InputData

#Fastapi component

app = FastAPI()

@app.get("/secure")
def secure_route(user: str = Depends(check_creds)):
    return {"message": "authentication successful"}

@app.get("/", response_class=FileResponse)
async def home():
    return 'static/index.html'

#viewpoint end function

@app.get("/form", response_class=FileResponse)
async def form():
    return 'static/psycho.html'

#json input
@app.post("/submit")
async def submit(pdata: InputData):
    with open('data/input.json', 'w') as fout:
        fout.write(pdata.model_dump_json())
    return {"message": "Form was submitted successfully"}

#@app.get("/analyze")
#async def analyze():
  #  try:
   #     analysis.main()
    #    return{"message": "Form was analyzed successfully"}
    #except Exception as e:
     #   return {"message": str(e)}

@app.get("/view/input", response_class=FileResponse)
async def view_input():
    return "data/input.json"
