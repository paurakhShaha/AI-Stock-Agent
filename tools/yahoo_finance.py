import yfinance as yf


def get_market_data(ticker):

    stock = yf.Ticker(ticker)


    # Current price
    info = stock.info


    market_data = {

        "ticker": ticker,


        "company": {
            "name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "country": info.get("country"),
        },


        "price": {

            "current":
                info.get("currentPrice"),

            "previous_close":
                info.get("previousClose"),

            "52_week_high":
                info.get("fiftyTwoWeekHigh"),

            "52_week_low":
                info.get("fiftyTwoWeekLow"),

        },


        "valuation": {

            "market_cap":
                info.get("marketCap"),

            "pe_ratio":
                info.get("trailingPE"),

            "forward_pe":
                info.get("forwardPE"),

            "price_to_book":
                info.get("priceToBook"),

            "peg_ratio":
                info.get("pegRatio"),

        },


        "financial_health": {

            "revenue":
                info.get("totalRevenue"),

            "profit":
                info.get("netIncomeToCommon"),

            "profit_margin":
                info.get("profitMargins"),

            "debt_to_equity":
                info.get("debtToEquity"),

            "roe":
                info.get("returnOnEquity"),

        },


        "dividend": {

            "yield":
                info.get("dividendYield"),

            "rate":
                info.get("dividendRate")

        }

    }


    return market_data

def get_price_history(ticker):

    stock = yf.Ticker(ticker)


    history = stock.history(
        period="1y"
    )


    return {

        "dates":
            history.index.strftime("%Y-%m-%d").tolist(),


        "close":
            history["Close"].round(2).tolist(),


        "volume":
            history["Volume"].tolist()

    }