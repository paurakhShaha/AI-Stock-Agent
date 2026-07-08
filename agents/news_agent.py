from google import genai
from google.genai import types
from dotenv import dotenv_values
import json

from tools.news_api import get_stock_news


config = dotenv_values(".env")

client = genai.Client(
    api_key=config["GEMINI_API_KEY"]
)


class NewsAgent:

    def __init__(self):

        with open("prompts/news_prompt.txt", encoding="utf-8") as f:
            self.system_prompt = f.read()


    def analyze(self, ticker):

        # Fetch news
        news = get_stock_news(ticker)


        prompt = f"""
{self.system_prompt}

Stock ticker:
{ticker}

News:
{json.dumps(news, indent=2)}
"""


        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )


        try:
            analysis = json.loads(response.text)

        except json.JSONDecodeError:
            analysis = {
                "decision": "UNKNOWN",
                "confidence": 0,
                "reasoning": "Model returned invalid JSON"
            }


        return {
            "agent": "news_agent",
            "ticker": ticker,
            "analysis": analysis,
            "metadata": {
                "prompt_tokens": response.usage_metadata.prompt_token_count,
                "response_tokens": response.usage_metadata.candidates_token_count,
                "total_tokens": response.usage_metadata.total_token_count
            }
        }