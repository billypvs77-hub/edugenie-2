from fastapi import FastAPI, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from qna import answer_question_with_gemini
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
   return templates.TemplateResponse(request, "index.html")

@app.get("/qa")
async def answer_question(question: str = Query(...)):
    answer = answer_question_with_gemini(question)
    return {"answer": answer}

@app.get("/summarize")
async def summarize(text: str = Query(...)):
    summary = summarize_text(text)
    return {"summary": summary}

@app.get("/quiz")
async def quiz(topic: str = Query(...)):
    result = generate_quiz(topic)
    return {"quiz": result}

@app.get("/learn/recommendations")
async def learning_recommendation_api(topic: str = Query(...)):
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}