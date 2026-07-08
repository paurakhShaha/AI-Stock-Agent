import yfinance as yf


def validate_ticker(ticker):

    stock = yf.Ticker(ticker)

    try:
        info = stock.info

        if not info:
            return False

        if info.get("regularMarketPrice") is None and info.get("currentPrice") is None:
            return False

        return True

    except Exception:
        return False