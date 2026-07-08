import json
import os

from orchestrator.orchestrator import StockAnalysisOrchestrator



class BatchAnalysisAgent:


    def __init__(self):

        self.orchestrator = StockAnalysisOrchestrator()



    def load_stocks(self):

        with open(
            "config/stocks.json"
        ) as f:

            data=json.load(f)

        return data["stocks"]



    def run(self):


        stocks=self.load_stocks()


        reports=[]


        for ticker in stocks:


            print(
                f"Analyzing {ticker}"
            )


            try:


                result=self.orchestrator.analyze(
                    ticker
                )


                reports.append(
                    result
                )


            except Exception as e:


                reports.append({

                    "ticker":ticker,

                    "error":str(e)

                })



        return reports