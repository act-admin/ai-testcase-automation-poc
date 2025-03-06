import openai
import os
import re  # Import regex for cleaning script

# Load Azure OpenAI credentials
AZURE_OPENAI_API_KEY = "77fcec110948487fb359f6c5b5507418"
AZURE_OPENAI_ENDPOINT = "https://act-azure-mvp.openai.azure.com/"
AZURE_DEPLOYMENT_NAME = "act-poc"  # e.g., "gpt-4", "gpt-3.5-turbo"

# Set API base for Azure OpenAI
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_version = "2023-09-15-preview"  # Update if needed

def clean_test_script(script):
    """Removes markdown formatting (triple backticks) from the test script."""
    return re.sub(r"```python|```", "", script).strip()

def generate_test_cases_and_script(user_story):
    prompt = f"Generate test cases and a Selenium Python test script for the following user story:\n\n{user_story}"

    try:
        response = openai.ChatCompletion.create(
            engine=AZURE_DEPLOYMENT_NAME,  # Use your Azure deployment name
            messages=[{"role": "system", "content": "You are a test automation expert."},
                      {"role": "user", "content": prompt}],
            max_tokens=800
        )
        
        generated_text = response["choices"][0]["message"]["content"].strip()

        # Extract test cases and script
        if "Test Script:" in generated_text:
            test_cases = generated_text.split("Test Script:")[0].strip()
            test_script = generated_text.split("Test Script:")[-1].strip()
            test_script = clean_test_script(test_script)  # Remove any Markdown formatting
        else:
            test_cases = generated_text
            test_script = "No test script generated."

        return test_cases, test_script

    except Exception as e:
        return f"Error generating test cases: {str(e)}", ""
