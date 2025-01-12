from fastapi import FastAPI, Form, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.services.qa_model import QA_Model 
from .utils.logger import logger

qa_model = QA_Model()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application is starting up.")
    yield
    logger.info("Application is shutting down.")

app = FastAPI(title="Question Answering System", description="A simple question answering system using BERT", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class QuestionRequest(BaseModel):
    context: str
    question: str

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/check")
def read_check():
    return {"status": "ok"}

@app.post("/answer/")
async def answer_question(request: QuestionRequest):
    context = request.context
    question = request.question
    
    if not context or not question:
        return JSONResponse({"error": "Context and question are required."}, status_code=400)
    
    answer = qa_model.answer_question(context, question)
    
    return JSONResponse({"answer": answer})

