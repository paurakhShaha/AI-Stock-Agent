import json

from tools.yahoo_finance import get_market_data


class MarketDataAgent:


    def __init__(self):

        self.name = "market_data_agent"



    def analyze(self, ticker):


        data = get_market_data(ticker)


        return {

            "agent": self.name,

            "ticker": ticker,

            "data": data

        }