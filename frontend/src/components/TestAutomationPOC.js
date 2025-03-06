import React, { useState } from "react";
import axios from "axios";
import { FaPlay, FaCheckCircle, FaSpinner } from "react-icons/fa";
import SyntaxHighlighter from "react-syntax-highlighter";
import { vs2015 } from "react-syntax-highlighter/dist/esm/styles/hljs";
import "../App.css";

const TestAutomationPOC = () => {
  const [userStory, setUserStory] = useState("");
  const [testCases, setTestCases] = useState("");
  const [testScript, setTestScript] = useState("");
  const [testReport, setTestReport] = useState("");
  const [loading, setLoading] = useState(false);

  const generateTestCases = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:8000/api/generate-test-cases", {
        userStory,
      });
      setTestCases(response.data.testCases);
      setTestScript(response.data.testScript);
    } catch (error) {
      console.error("Error generating test cases:", error);
    }
    setLoading(false);
  };

  const executeTest = async () => {
    try {
      const response = await axios.post("http://localhost:8000/api/execute-tests", {
        testScript,
      });
      setTestReport(response.data.report);
    } catch (error) {
      console.error("Error executing test:", error);
    }
  };

  return (
    <div className="ai-studio">
      <header className="ai-studio-header">
        <div className="company-logo">
          <img src="/Dac-final logo.png" alt="DAC Logo" />
        </div>
      </header>

      <main className="ai-studio-container">
        <h1 className="ai-studio-title">
          <span role="img" aria-label="rocket">
            🚀
          </span>{" "}
          AI Powered TestCase Automation Studio
        </h1>

        <section className="main-layout">
          <div className="panel user-story-section">
            <label className="panel-title">Enter Your User Story</label>
            <textarea
              className="panel-textarea"
              placeholder="Describe the functionality to test..."
              value={userStory}
              onChange={(e) => setUserStory(e.target.value)}
            />
            {loading && (
              <div className="loading-spinner">
                <FaSpinner className="animate-spin" />
              </div>
            )}
          </div>

          <div className="button-section">
            <button
              className="action-button"
              onClick={generateTestCases}
              disabled={loading}
            >
              {loading ? <FaSpinner className="animate-spin" /> : <><FaPlay /> Generate Test Cases</>}
            </button>
          </div>

          <div className="panel test-cases-section">
            <h2 className="panel-title">
              <span role="img" aria-label="check mark">
                ✅
              </span>{" "}
              Generated Test Cases
            </h2>
            <pre className="panel-content">{testCases || "Test cases will appear here..."}</pre>
          </div>
        </section>

        {testScript && (
          <section className="panel full-width">
            <h2 className="panel-title">
              <span role="img" aria-label="scroll">
                📜
              </span>{" "}
              Generated Test Script
            </h2>
            <div className="code-block">
              <SyntaxHighlighter language="python" style={vs2015}>
                {testScript}
              </SyntaxHighlighter>
            </div>
          </section>
        )}

        {testScript && (
          <div className="button-section full-width">
            <button className="action-button" onClick={executeTest}>
              <FaCheckCircle /> Execute Tests
            </button>
          </div>
        )}

        {testReport && (
          <section className="panel full-width">
            <h2 className="panel-title">
              <span role="img" aria-label="chart">
                📊
              </span>{" "}
              Test Execution Report
            </h2>
            <pre className="panel-content">{testReport}</pre>
          </section>
        )}

        <footer className="ai-studio-footer">
          Powered by <span className="footer-highlight">DAC Platforms & Solutions</span>
        </footer>
      </main>
    </div>
  );
};

export default TestAutomationPOC;