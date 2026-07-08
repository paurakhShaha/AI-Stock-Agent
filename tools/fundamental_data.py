import yfinance as yf


def get_fundamental_data(ticker):

    stock = yf.Ticker(ticker)


    info = stock.info


    income = stock.financials

    balance = stock.balance_sheet

    cashflow = stock.cashflow



    data = {


        "company": {

            "name":
                info.get("longName"),

            "sector":
                info.get("sector")

        },


        "valuation": {

            "market_cap":
                info.get("marketCap"),

            "pe_ratio":
                info.get("trailingPE"),

            "forward_pe":
                info.get("forwardPE"),

            "peg_ratio":
                info.get("pegRatio")

        },


        "profitability": {

            "profit_margin":
                info.get("profitMargins"),

            "operating_margin":
                info.get("operatingMargins"),

            "roe":
                info.get("returnOnEquity"),

            "roa":
                info.get("returnOnAssets")

        },


        "growth": {

            "revenue_growth":
                info.get("revenueGrowth"),

            "earnings_growth":
                info.get("earningsGrowth")

        },


        "financial_health": {

            "debt_to_equity":
                info.get("debtToEquity"),

            "current_ratio":
                info.get("currentRatio")

        }

    }


    return data