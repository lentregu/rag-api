# RAG API Project

## **Description**

This project is a practical implementation of a **Retrieval-Augmented Generation (RAG)** application. It uses **LangChain**, **Llama**, and other AI tools to build a question-answering system that retrieves context from external documents (e.g., web pages) and provides meaningful responses.

The main goal of this project is to explore how to build a **Retrieval-Augmented Generation (RAG)** system to enhance a general-purpose LLM and tackle some of its common limitations like:

- **Inaccurate responses**:  
  LLMs can sometimes provide incorrect answers. Additionally, their responses might occasionally reflect biases or prejudices.  

- **Static knowledge**:  
  LLMs have their knowledge fixed at a specific point in time, based on the training data. They don’t incorporate new information unless retrained.  

- **Hallucinations**:  
  When they lack enough context or data to answer a question, they might make up an answer.  

- **Lack of specialization**:  
  General-purpose LLMs are trained on broad, generic information. In specialized environments, such as those with precise company-specific data, they may not deliver accurate or relevant responses.  

- **High costs**:  
  Generic LLMs can be expensive to use and scale due to their size and broad training.  

The project employs:
- **LangChain** for managing the flow of data between components.
- **Llama-based models** for generating intelligent responses.
- **Chroma** for efficient vector-based similarity search.
- **FastAPI** for exposing a clean RESTful API interface.

---

## **Features**

- Retrieve document content dynamically from the web.
- Use embeddings to create a vector store for efficient similarity-based search.
- Answer questions based on retrieved context or provide general answers when the context is insufficient.
- Modular design to facilitate scalability and learning.

---

## **Project Structure**

```plaintext
rag_api/
│
├── app/
│   ├── __init__.py                   # Initializes the app module
│   ├── api/
│   │   ├── __init__.py               # Initializes the API module
│   │   └── endpoints.py              # Defines the FastAPI routes
│   ├── services/
│   │   ├── __init__.py               # Initializes the services module
│   │   ├── document_loader.py        # Handles document loading from web URLs
│   │   ├── qa_system.py              # Logic for QA system initialization
│   │   └── question_request.py       # Handles QA system queries
│   └── main.py                       # Entry point of the application
├── requirements.txt                  # Dependencies for the project
└── .venv/                             # Virtual environment
```

## **Requirements**

Before running the project, make sure you have the following installed:

- **Python 3.8** or newer
- **llama3** model for the LLM (Large Language Model)
- Libraries listed in the `requirements.txt` file (Install these dependencies using `pip`).

## **Setup and Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/lentregu/rag-api.git
cd rag-api
```

To set up a virtual environment and install the necessary dependencies, follow these steps:

### **2. Set Up a Virtual Environment**

Create and activate a Python virtual environment to isolate dependencies:

```bash
# Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**
Install the required libraries from the requirements.txt file:

```bash
pip install -r requirements.txt
```
### **4. Install llama3 LLM model**
 Install the `llama3` model by running: 
```bash
ollama pull llama3
```

## **Running the Application**

### **1. Start the FastAPI Server**

Run the application using uvicorn:

```bash
uvicorn app.main:app --reload
```
The server will start at http://127.0.0.1:8000.

## **Access the API Documentation**

FastAPI provides interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## **How to Use**

### **Endpoint: `/ask`**

- **Method**: `GET`
- **Description**: Retrieves an answer to a question based on content loaded from a specified URL.

#### **Query Parameters**:
- `question` (required): The question you want the system to answer.
- `url` (required): The URL of the web page to retrieve context from.

### **Example Request**

```bash
curl "http://127.0.0.1:8000/ask/?question=Who+is+Guille+Rosas?&url=https://es.wikipedia.org/wiki/Guille_Rosas"
```

### **Example Response**

```json
{
  "answer": "Based on the provided context, it appears that Guille Rosas is a soccer player who plays as a right back for Sporting de Gijón...."
}
```
