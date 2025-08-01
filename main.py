from helper import *
import pandas as pd
import yfinance as yf
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from scipy.signal import find_peaks

beautiful_print()

# Select the stock
usr_input = input("\n\n\n  Insert the stock name (e.g.: APPLE, MICROSOFT, GOOGLE, META, AMAZON) or press 'q to exit:\n  ")
if usr_input == 'q':
    print('Adios!')
    exit(1)
stock_name = usr_input
company_to_ticker = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'GOOGLE': 'GOOGL',
    'META': 'META',
    'AMAZON': 'AMZN',
    # Add more as needed
}

stock_sel = company_to_ticker[stock_name]
data = yf.download(stock_sel, period='1mo', progress=False, auto_adjust=True)['Close']
data = data.dropna()
# data.plot()

# Detect peaks and troughs in the analyzed period
peaks, _ = find_peaks(data.values.ravel(), distance=10)
# troughs, _ = find_peaks(-data.values.ravel(), distance=10)

# Init. the model
model = OllamaLLM(model='llama3.2')  # Adjust version if needed
prompt = ChatPromptTemplate.from_template("""
You are a financial analyst AI.

Stock: {stock}
Date: {date}
Price: {price}

Relevant News:
{news}

Based on the above information, briefly explain if and how the news might have influenced the stock price movement.
""")

chain = prompt | model

# Loop through a few peaks
for idx in peaks[:3]:  # Limit to 3 for demo
    date = data.index[idx]
    price = round(data.iloc[idx], 2).values[0]
    news = fetch_news(stock_name, date)

    result = chain.invoke({
        "stock": stock_name,
        "date": date.strftime("%Y-%m-%d"),
        "price": price,
        "news": news
    })

    print(f"\n📈 Date: {date.strftime('%Y-%m-%d')} - Price: ${price}")

    print("📰 Correlation Analysis:\n", result)
