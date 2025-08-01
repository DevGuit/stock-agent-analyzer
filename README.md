# Stock Agent Analysis

![Stock Agent Analysis Demo](demo.gif)

This project analyzes stock peaks fetching news articles and using a large language model to understanding the reasons of the stock variation.

## Prerequisites

- Python 3.12+
- [Ollama](https://ollama.ai/) installed and running.
- llama3.2 installed (ollama pull llama3.2)
- A NewsAPI API key.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd stock-sentiment
    ```

2.  **Install uv:**
    ```bash
    pip install uv
    ```

3.  **Install the dependencies and virtual environment:**
    ```bash
    uv sync
    ```

## Configuration

1.  Create a `.env` file in the root of the project.
2.  Add your NewsAPI key to the `.env` file:
    ```
    API_NEWS_KEY=your_api_key
    ```

## Usage

Run the main script:
```bash
uv run main.py
```
