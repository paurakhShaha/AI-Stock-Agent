import json

from agents.fundamental_agent import FundamentalAgent



ticker=input(
    "Ticker: "
)


agent=FundamentalAgent()


result=agent.analyze(
    ticker
)


print(
    json.dumps(
        result,
        indent=4
    )
)