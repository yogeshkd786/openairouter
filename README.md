# OpenRouter Inference Examples

This repository contains Python scripts demonstrating how to connect to and interact with large language models hosted on [OpenRouter.ai](https://openrouter.ai/).

## What is OpenRouter?

OpenRouter is a unified API for accessing a wide variety of large language models (LLMs) from different providers like OpenAI, Google, Anthropic, Mistral, and more. It acts as a single, consistent interface, allowing developers to:

-   **Switch between models easily** without changing their code significantly.
-   **Access models** that might not be publicly available or easy to get credentials for.
-   **Get fallback options** and routing to the best model for a given task.
-   **Monitor costs and usage** across all models in one place.

It simplifies the process of experimenting with and integrating multiple LLMs into an application.

## Project Structure

This project provides two distinct examples of how to use the OpenRouter API, located in their respective folders:

### 1. `openaisdk/`

-   **Method:** Uses the standard `openai` Python library.
-   **How it works:** The OpenAI library can be configured to point to a different API endpoint. This script demonstrates how to set the `base_url` to OpenRouter's endpoint, allowing you to use the familiar OpenAI SDK syntax to interact with any model available on OpenRouter.
-   **Use Case:** This is a great option if you are already familiar with the OpenAI library or want a straightforward, direct way to send requests.

### 2. `langchain/`

-   **Method:** Uses the `LangChain` framework.
-   **How it works:** LangChain is a powerful framework for building applications with LLMs. It provides abstractions and chains for more complex workflows. This script shows how to configure a LangChain `ChatOpenAI` object to use OpenRouter as its backend.
-   **Use Case:** This approach is ideal for building more complex applications that involve prompt templates, chains of thought, agents, or other advanced LangChain features.

## Getting Started

Each sub-directory (`openaisdk/` and `langchain/`) contains its own `README.md` file with specific instructions on how to set up the environment, install dependencies, and run the respective script.

Please refer to the README file within each folder to get started with the examples.
