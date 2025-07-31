from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet

load_dotenv()
newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY"))

def fetch_news(company, date):
    from_date = date.strftime('%Y-%m-%d')
    to_date = (date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')

    response = newsapi.get_everything(
        q=company,
        from_param=from_date,
        to=to_date,
        sort_by='popularity',
        language='en',
        page_size=5
    )
    articles = response.get('articles', [])
    if not articles:
        return "No news found."

    return "\n".join([f"- {a['title']}" for a in articles])


def beautiful_print():
    console = Console()

    # Create stylized ASCII text
    fig = Figlet(font='slant')  # You can try 'standard', 'big', 'block', etc.
    ascii_art = fig.renderText('devguit')

    # Display with rich panel
    console.print(Panel(ascii_art, title="Welcome", subtitle="devguit terminal", border_style="bold cyan"))
