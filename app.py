import os, sys
from fastapi import FastAPI, HTTPException
from fastapi import Body
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
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

pipeline = PredictionPipeline()

@app.get("/", tags=['authentications'])
async def read_root():
    return RedirectResponse('/docs')

@app.get("/health", tags=['authentications'])
async def health():
    return {"status": "ok"}



@app.post("/get_summary", tags=['authentications'])
async def get_summary(text: str = Body(..., embed=True)):
    # Validate input
    if not text or not isinstance(text, str):
        raise HTTPException(status_code=400, detail="Invalid input: text must be a non-empty string.")

    try:
        out = pipeline.prediction(text)

        return {'prediction': out}
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)