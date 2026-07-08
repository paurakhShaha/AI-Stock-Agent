from tools.macro_data import get_macro_data



class MacroAgent:


    def __init__(self):

        self.name="macro_agent"



    def analyze(self,ticker):


        data=get_macro_data()



        score=50


        positives=[]

        risks=[]



        # Inflation


        inflation=data.get(
            "inflation"
        )


        if inflation:


            if inflation < 5:

                score+=10

                positives.append(
                    "Inflation environment stable"
                )


            else:

                score-=10

                risks.append(
                    "High inflation pressure"
                )



        # Interest Rate


        rate=data.get(
            "interest_rate"
        )


        if rate:


            if rate < 4:

                score+=10

                positives.append(
                    "Lower interest rate environment"
                )


            else:

                score-=10

                risks.append(
                    "High interest rates"
                )



        # Unemployment


        unemployment=data.get(
            "unemployment"
        )


        if unemployment:


            if unemployment < 6:

                score+=5

                positives.append(
                    "Healthy labor market"
                )


            else:

                score-=5

                risks.append(
                    "Weak employment"
                )



        score=max(
            0,
            min(score,100)
        )



        if score>=75:

            environment="POSITIVE"


        elif score>=50:

            environment="NEUTRAL"


        else:

            environment="NEGATIVE"



        return {


            "agent":
                self.name,


            "ticker":
                ticker,


            "macro_score":
                score,


            "environment":
                environment,


            "economic_data":
                data,


            "tailwinds":
                positives,


            "headwinds":
                risks,


            "confidence":
                score/100

        }