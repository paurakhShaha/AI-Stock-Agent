import json

from agents.technical_agent import TechnicalAgent



ticker=input(
    "Ticker: "
)


agent=TechnicalAgent()


result=agent.analyze(
    ticker
)


print(
    json.dumps(
        result,
        indent=4
    )
)