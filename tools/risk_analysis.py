import yfinance as yf
import numpy as np



def calculate_risk_data(ticker):


    stock = yf.Ticker(ticker)


    history = stock.history(
        period="1y"
    )


    info = stock.info



    close = history["Close"]



    # Daily returns

    returns = close.pct_change().dropna()



    # Volatility

    volatility = (
        returns.std()
        *
        np.sqrt(252)
    )



    # Maximum drawdown

    rolling_max = close.cummax()

    drawdown = (
        close - rolling_max
    ) / rolling_max


    max_drawdown = drawdown.min()



    return {


        "volatility":
            round(
                volatility,
                3
            ),


        "maximum_drawdown":
            round(
                max_drawdown,
                3
            ),


        "beta":
            info.get(
                "beta"
            ),


        "debt_to_equity":
            info.get(
                "debtToEquity"
            ),


        "current_ratio":
            info.get(
                "currentRatio"
            ),


        "market_cap":
            info.get(
                "marketCap"
            )

    }