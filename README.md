# ai-testcase-automation-poc
 PoC Outline: Automated Test Case Generation System


# Running the Project
Install Backend Dependencies

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm start

# Access the app at:
Frontend: http://localhost:3000
Backend: http://localhost:8000/docs (FastAPI interactive docs)
