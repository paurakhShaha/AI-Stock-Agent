from tools.fundamental_data import get_fundamental_data



class FundamentalAgent:


    def __init__(self):

        self.name = "fundamental_agent"



    def analyze(self,ticker):


        data = get_fundamental_data(
            ticker
        )


        score = 50


        strengths=[]

        weaknesses=[]



        profitability = data["profitability"]

        growth = data["growth"]

        health = data["financial_health"]

        valuation = data["valuation"]



        # Profit Margin

        margin = profitability.get(
            "profit_margin"
        )


        if margin:

            if margin > 0.15:

                score += 10

                strengths.append(
                    "Strong profit margin"
                )

            else:

                score -= 5

                weaknesses.append(
                    "Low profit margin"
                )



        # ROE

        roe = profitability.get(
            "roe"
        )


        if roe:

            if roe > 0.15:

                score += 10

                strengths.append(
                    "Good return on equity"
                )

            else:

                score -= 5



        # Revenue growth

        revenue_growth = growth.get(
            "revenue_growth"
        )


        if revenue_growth:

            if revenue_growth > 0.10:

                score += 10

                strengths.append(
                    "Strong revenue growth"
                )

            else:

                weaknesses.append(
                    "Slow revenue growth"
                )



        # Debt

        debt = health.get(
            "debt_to_equity"
        )


        if debt:

            if debt < 100:

                score += 5

                strengths.append(
                    "Healthy debt level"
                )

            else:

                score -= 10

                weaknesses.append(
                    "High debt"
                )



        # Valuation

        pe = valuation.get(
            "pe_ratio"
        )


        if pe:

            if pe < 25:

                score += 5

                strengths.append(
                    "Reasonable valuation"
                )

            elif pe > 50:

                score -= 10

                weaknesses.append(
                    "Expensive valuation"
                )



        score=max(
            0,
            min(score,100)
        )



        return {


            "agent":
                self.name,


            "ticker":
                ticker,


            "fundamental_score":
                score,


            "business_quality":
                (
                    "STRONG"
                    if score>=75
                    else
                    "AVERAGE"
                    if score>=50
                    else
                    "WEAK"
                ),



            "data":
                data,


            "strengths":
                strengths,


            "weaknesses":
                weaknesses,


            "confidence":
                score/100

        }