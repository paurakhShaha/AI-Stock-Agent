from agents.market_agent import MarketDataAgent
from agents.news_agent import NewsAgent
from agents.technical_agent import TechnicalAgent
from agents.fundamental_agent import FundamentalAgent
from agents.risk_agent import RiskAgent
from agents.macro_agent import MacroAgent
from agents.devil_agent import DevilAgent
from agents.committee_agent import InvestmentCommitteeAgent
from agents.report_agent import ReportGeneratorAgent
from tools.ticker_validator import validate_ticker


class StockAnalysisOrchestrator:



    def analyze(self,ticker):
        if not validate_ticker(ticker):

            return {
                "error": f"Invalid ticker symbol: {ticker}",
                "message": "Please enter a valid Yahoo Finance ticker."
            }

        market = MarketDataAgent().analyze(
            ticker
        )


        news = NewsAgent().analyze(
            ticker
        )


        technical = TechnicalAgent().analyze(
            ticker
        )


        fundamental = FundamentalAgent().analyze(
            ticker
        )


        risk = RiskAgent().analyze(
            ticker
        )


        macro = MacroAgent().analyze(
            ticker
        )


        combined={


            "market":
            market,


            "news":
            news,


            "technical":
            technical,


            "fundamental":
            fundamental,


            "risk":
            risk,


            "macro":
            macro

        }



        devil = DevilAgent().analyze(

            ticker,

            combined

        )


        combined["devil"]=devil



        decision = InvestmentCommitteeAgent().analyze(

            ticker,

            combined

        )


        combined["decision"]=decision



        report = ReportGeneratorAgent().generate(

            ticker,

            combined

        )


        return report