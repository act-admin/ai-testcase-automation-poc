import os
import subprocess
import traceback

def execute_test_script(script_content):
    file_path = os.path.abspath("temp_test_script.py")  # Use absolute path
    report_dir = os.path.abspath("reports")
    report_path = os.path.join(report_dir, "test_report.txt")

    # Debug: Print script content before writing
    print("🔹 Writing Test Script:\n", script_content)

    # Ensure report directory exists
    os.makedirs(report_dir, exist_ok=True)

    try:
        # Write the test script
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(script_content)

        # Debug: Confirm file content
        with open(file_path, "r", encoding="utf-8") as file:
            print("✅ Written Test Script:\n", file.read())

        # Execute script and capture output
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        output = f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}\n"

    except Exception as e:
        output = f"❌ ERROR:\n{traceback.format_exc()}"

    # Save output in reports folder
    try:
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write(output)
        print(f"✅ Report saved at: {report_path}")
    except Exception as e:
        print(f"❌ Failed to write report: {e}")

    return output
