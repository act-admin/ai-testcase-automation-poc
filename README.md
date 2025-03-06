# AI Test Case Automation PoC

## Overview
This project is a Proof of Concept (PoC) for an AI-powered automated test case generation system. It leverages AI to generate test cases based on user stories and executes them using Selenium-based automation scripts.

## Features
- AI-generated test cases from user stories
- Automated test script generation
- Execution of test cases using Selenium
- Test execution reports

## Tech Stack
- **Frontend:** React, Tailwind CSS
- **Backend:** FastAPI, Python, OpenAI API
- **Testing Framework:** Selenium, Unittest
- **Database (if needed):** SQLite / PostgreSQL

## Installation & Setup

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-testcase-automation-poc.git
   cd ai-testcase-automation-poc
   ```
2. Navigate to the backend directory:
   ```sh
   cd backend
   ```
3. Create and activate a virtual environment:
   - On macOS/Linux:
     ```sh
     python -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Start the backend server:
   ```sh
   uvicorn main:app --reload
   ```
6. Access FastAPI interactive docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend application:
   ```sh
   npm start
   ```
4. Access the app at: [http://localhost:3000](http://localhost:3000)

## Usage
1. Enter a user story in the provided text field.
2. Click **Generate Test Cases** to generate AI-powered test cases.
3. Review the test cases and Selenium test scripts.
4. Click **Execute Tests** to run the test scripts.
5. View the test execution report in the UI.

## Future Enhancements
- Integration with CI/CD pipelines
- Support for multiple test frameworks (PyTest, JUnit, etc.)
- Enhanced AI-driven test case optimization
- Database storage for test cases and execution history

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License.

---

_Developed by ❤️ DAC Platforms & Solutions.
