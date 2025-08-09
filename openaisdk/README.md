# OpenAI SDK with OpenRouter Example

This script demonstrates how to use the OpenAI Python library to connect to the OpenRouter API.

## Setup and Execution Guide

### 1. Create a Virtual Environment

It is recommended to use a virtual environment to manage project dependencies. This project uses `uv` for environment and package management.

First, create the virtual environment:

```bash
uv venv
```

This will create a `.venv` directory in your project folder.

Next, activate the virtual environment.

**On Windows:**

```bash
.venv\Scripts\activate
```

**On macOS and Linux:**

```bash
source .venv/bin/activate
```

### 2. Set Up Your API Key

The script needs your OpenRouter API key to authenticate.

1.  Create a file named `.env` in this directory.
2.  Add your API key to the `.env` file as follows:

    ```
    OPENROUTER_API_KEY="your-api-key-here"
    ```

    Replace `"your-api-key-here"` with your actual OpenRouter API key.

### 3. Install Dependencies

Install the required Python libraries using `uv` and the `requirements.txt` file:

```bash
uv pip install -r requirements.txt
```

### 4. Run the Script

Once your environment is set up and the dependencies are installed, you can run the Python script:

```bash
python openaisdk.py
```

The script will then connect to OpenRouter, send a request, and print the response to the console.
