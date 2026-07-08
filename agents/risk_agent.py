from tools.risk_analysis import calculate_risk_data



class RiskAgent:


    def __init__(self):

        self.name="risk_agent"



    def analyze(self,ticker):


        data = calculate_risk_data(
            ticker
        )


        score = 50


        warnings=[]

        positives=[]



        # Volatility


        volatility=data["volatility"]


        if volatility:


            if volatility < 0.25:

                score += 10

                positives.append(
                    "Low volatility"
                )


            elif volatility > 0.50:

                score -= 15

                warnings.append(
                    "High price volatility"
                )



        # Drawdown


        drawdown=data[
            "maximum_drawdown"
        ]


        if drawdown:


            if drawdown > -0.20:

                score += 10

                positives.append(
                    "Small historical decline"
                )


            elif drawdown < -0.40:

                score -= 15

                warnings.append(
                    "Large historical drawdown"
                )



        # Beta


        beta=data["beta"]


        if beta:


            if beta < 1:

                score += 5

                positives.append(
                    "Lower market sensitivity"
                )


            elif beta > 1.5:

                score -= 10

                warnings.append(
                    "High market sensitivity"
                )



        # Debt


        debt=data[
            "debt_to_equity"
        ]


        if debt:


            if debt > 150:

                score -= 10

                warnings.append(
                    "High debt"
                )



        score=max(
            0,
            min(score,100)
        )



        if score >=75:

            risk_level="LOW"


        elif score >=50:

            risk_level="MEDIUM"


        else:

            risk_level="HIGH"



        return {


            "agent":
                self.name,


            "ticker":
                ticker,


            "risk_score":
                score,


            "risk_level":
                risk_level,


            "metrics":
                data,


            "positive_factors":
                positives,


            "warnings":
                warnings,


            "confidence":
                score/100

        }