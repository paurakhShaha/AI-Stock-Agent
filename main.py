import json

from orchestrator.orchestrator import StockAnalysisOrchestrator



ticker=input(
    "Enter stock ticker: "
)



agent=StockAnalysisOrchestrator()



result=agent.analyze(
    ticker
)



print("\n===== INVESTMENT REPORT =====")


print(
    json.dumps(
        result,
        indent=4
    )
)