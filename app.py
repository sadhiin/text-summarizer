import os, sys
from fastapi.templating import Jinja2Templates
from starlette.requests import RedirectResponse
from fastapi.responses import Response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.textSummarizer.pipeline import PredictionPipeline

app = FastAPI()
## allows cors

origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)


@app.get("/", tags=['authentications'])
async def read_root():
    return RedirectResponse('/docs')

@app.get("/health", tags=['authentications'])
async def health():
    return {"status": "ok"}

@app.get('/train')
async def train():
    os.system('python main.py')
    return Response(content='Training Completed')


@app.post("/get_summary", tags=['authentications'])
async def get_summary(text):
    try:
        out = PredictionPipeline().prediction(text)
        
        return {'prediction': out}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)