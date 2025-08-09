# LangChain with OpenRouter Example

This script demonstrates how to use LangChain with the OpenRouter API to create a simple LLM chain.

## Setup and Execution Guide

Follow these steps to set up your environment and run the script.

### 1. Create and Activate a Virtual Environment

Using a virtual environment is crucial for managing project-specific dependencies.

**Create the environment (using uv):**
```bash
uv venv
```

**Activate the environment:**

*   **On Windows:**
    ```bash
    .venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

### 2. Configure Environment Variables

The script uses a `.env` file to load necessary credentials and configuration.

1.  Make sure you have a `.env` file in the same directory as the script.
2.  This file should contain the following variables:

    ```dotenv
    # Your unique API key from OpenRouter.ai
    OPENROUTER_API_KEY="your-openrouter-api-key"

    # The base URL for the OpenRouter API
    OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"

    # (Optional) For tracking on the OpenRouter dashboard
    YOUR_SITE_URL="http://localhost:3000"
    YOUR_SITE_NAME="My LangChain App"
    ```

    Replace the placeholder values with your actual information.

### 3. Install Dependencies

Install the required Python libraries from the `requirements.txt` file.

```bash
uv pip install -r requirements.txt
```

### 4. Update the Model Name

Before running, you need to specify which model you want to use. Open the `langchain_openrouter.py` file and replace `<model_name>` with the model of your choice (e.g., `"openai/gpt-4o"`).

### 5. Run the Script

Execute the script using Python:

```bash
python langchain_openrouter.py
```

The script will send the question to the specified model via OpenRouter and print the generated answer.
