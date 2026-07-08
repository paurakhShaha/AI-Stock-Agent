import yfinance as yf
import pandas as pd

from ta.momentum import RSIIndicator
from ta.trend import MACD, SMAIndicator, EMAIndicator


def get_technical_data(ticker):

    stock = yf.Ticker(ticker)


    df = stock.history(
        period="1y"
    )


    if df.empty:
        return {}


    close = df["Close"]


    # Moving averages

    sma_50 = SMAIndicator(
        close,
        window=50
    ).sma_indicator()


    sma_200 = SMAIndicator(
        close,
        window=200
    ).sma_indicator()



    # RSI

    rsi = RSIIndicator(
        close,
        window=14
    ).rsi()



    # MACD

    macd = MACD(
        close
    )


    latest = {

        "price":
            round(
                close.iloc[-1],
                2
            ),


        "sma_50":
            round(
                sma_50.iloc[-1],
                2
            ),


        "sma_200":
            round(
                sma_200.iloc[-1],
                2
            ),


        "rsi":
            round(
                rsi.iloc[-1],
                2
            ),


        "macd":
            round(
                macd.macd().iloc[-1],
                3
            ),


        "macd_signal":
            round(
                macd.macd_signal().iloc[-1],
                3
            )

    }


    return latest