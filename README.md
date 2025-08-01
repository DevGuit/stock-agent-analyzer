# Stock Sentiment Analysis

![Stock Sentiment Analysis Demo](demo.gif)

This project analyzes stock sentiment by fetching news articles and using a large language model to determine the sentiment of each article.

## Prerequisites

- Python 3.12+
- [Ollama](https://ollama.ai/) installed and running.
- A NewsAPI API key.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd stock-sentiment
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
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
python main.py
```
