from fastapi import FastAPI
from app.api.endpoints import ask_question

app = FastAPI()

app.include_router(ask_question, prefix="/ask", tags=["Questions"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)