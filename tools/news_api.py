import json
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

def compress_news(news_json):
    compressed = {
        "items": len(news_json.get("feed", [])),
        "articles": []
    }

    for article in news_json.get("feed", []):
        compressed_article = {
            "title": article.get("title"),
            "published": article.get("time_published"),
            "source": article.get("source"),
            "summary": article.get("summary", ""),

            "market_sentiment": {
                "label": article.get("overall_sentiment_label"),
                "score": round(article.get("overall_sentiment_score", 0), 3),
            },

            "topics": [
                {
                    "name": topic["topic"],
                    "relevance": round(float(topic["relevance_score"]), 2),
                }
                for topic in article.get("topics", [])
            ],

            "tickers": [
                {
                    "symbol": ticker["ticker"],
                    "relevance": round(float(ticker["relevance_score"]), 2),
                    "sentiment": ticker["ticker_sentiment_label"],
                    "score": round(float(ticker["ticker_sentiment_score"]), 2),
                }
                for ticker in article.get("ticker_sentiment", [])
            ]
        }

        compressed["articles"].append(compressed_article)

    return compressed






def get_stock_news(ticker):
    url = "https://www.alphavantage.co/query"

    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": ticker,
        "topics": "technology,finance",
        "sort": "LATEST",
        "limit": "10",
        "apikey": config["NEWS_API"],
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if "feed" in data:
        print(f"Retrieved {len(data['feed'])} articles.")

        compressed = compress_news(data)

        return compressed

    else:
        print("API Error:")
        print(json.dumps(data, indent=4))

        return {
            "items": 0,
            "articles": []
        }







