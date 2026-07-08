from tools.technical_indicators import get_technical_data



class TechnicalAgent:


    def __init__(self):

        self.name = "technical_agent"



    def analyze(self,ticker):


        data = get_technical_data(ticker)


        score = 50


        signals = []

        warnings = []


        price = data["price"]

        sma50 = data["sma_50"]

        sma200 = data["sma_200"]

        rsi = data["rsi"]

        macd = data["macd"]

        signal = data["macd_signal"]



        # Trend analysis

        if price > sma50:

            score += 10

            signals.append(
                "Price above 50 day average"
            )

        else:

            score -= 10

            warnings.append(
                "Price below 50 day average"
            )



        if price > sma200:

            score += 15

            signals.append(
                "Long term trend bullish"
            )

        else:

            score -= 15

            warnings.append(
                "Below 200 day average"
            )



        # RSI

        if rsi < 30:

            signals.append(
                "Oversold condition"
            )

            score += 5


        elif rsi > 70:

            warnings.append(
                "Overbought condition"
            )

            score -= 5



        # MACD

        if macd > signal:

            score += 10

            signals.append(
                "Positive MACD momentum"
            )

        else:

            score -= 10

            warnings.append(
                "Negative MACD momentum"
            )



        score = max(
            0,
            min(
                score,
                100
            )
        )



        return {


            "agent":
                self.name,


            "ticker":
                ticker,


            "technical_score":
                score,


            "trend":
                "BULLISH"
                if score >= 60
                else "BEARISH",



            "indicators":
                data,


            "signals":
                signals,


            "warnings":
                warnings,


            "confidence":
                score/100

        }