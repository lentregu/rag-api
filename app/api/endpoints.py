from fastapi import APIRouter, HTTPException
from app.services.question_request import get_qa_response

ask_question = APIRouter()

@ask_question.get("/")
async def ask_question_endpoint(question: str, url: str = None):
    # if not url:
    #     raise HTTPException(status_code=400, detail="URL parameter is required.")
    
    try:
        # Fetch the answer using the get_qa_response function
        response = get_qa_response(question, url)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
