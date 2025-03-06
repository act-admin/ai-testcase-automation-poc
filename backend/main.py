from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from test_generator import generate_test_cases_and_script
from test_executor import execute_test_script
from fastapi.middleware.cors import CORSMiddleware
import json


# Initialize FastAPI
app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change this for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define Input Models
class UserStoryInput(BaseModel):
    userStory: str

class TestScriptInput(BaseModel):
    testScript: str

# Generate Test Cases & Script
@app.post("/api/generate-test-cases")
def generate_test_cases(input_data: UserStoryInput):
    try:
        test_cases, test_script = generate_test_cases_and_script(input_data.userStory)

        response = {
            "testCases": test_cases.strip(),
            "testScript": test_script.strip()
        }

        print("DEBUG RESPONSE:", json.dumps(response, indent=2))  # Log response

        return response
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

# Execute Test Script
@app.post("/api/execute-tests")
def execute_tests(input_data: TestScriptInput):
    try:
        logging.info("Executing test script...")
        report = execute_test_script(input_data.testScript)
        
        logging.info("Test script executed successfully.")
        return {"report": report.strip()}

    except Exception as e:
        logging.error(f"Error executing test script: {str(e)}")
        raise HTTPException(status_code=500, detail="Test execution failed.")
