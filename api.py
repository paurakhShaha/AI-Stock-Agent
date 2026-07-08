from fastapi import FastAPI

from orchestrator.orchestrator import StockAnalysisOrchestrator


app = FastAPI()


agent = StockAnalysisOrchestrator()



@app.get("/")
def home():

    return {
        "status":"AI Stock Agent Running"
    }



@app.get("/analyze/{ticker}")
def analyze(ticker):

    result = agent.analyze(
        ticker
    )

    return result