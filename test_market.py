import json

from agents.market_agent import MarketDataAgent



ticker = input("Stock ticker: ")


agent = MarketDataAgent()


result = agent.analyze(ticker)


print(
    json.dumps(
        result,
        indent=4
    )
)