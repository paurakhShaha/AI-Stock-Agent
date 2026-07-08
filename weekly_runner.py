import json
from datetime import datetime

from orchestrator.orchestrator import StockAnalysisOrchestrator
from agents.report_agent import ReportGeneratorAgent
from tools.email_sender import send_email


def run_daily():

    with open("config/stocks.json", "r") as f:
        stocks = json.load(f)["stocks"]

    # Monday=0 ... Sunday=6
    day = datetime.today().weekday()

    if day >= len(stocks):
        print("No stock assigned for today.")
        return

    ticker = stocks[day]

    print(f"Today's stock: {ticker}")

    orchestrator = StockAnalysisOrchestrator()

    result = orchestrator.analyze(ticker)

    report = ReportGeneratorAgent().generate(
        ticker,
        result
    )

    send_email(
        subject=f"Daily AI Stock Report - {ticker}",
        body=report["report"]
    )