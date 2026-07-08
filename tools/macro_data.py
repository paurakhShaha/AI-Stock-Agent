import requests
from dotenv import dotenv_values


config = dotenv_values(".env")



def get_macro_data():


    data = {}



    # FRED API

    fred_key = config.get(
        "FRED_API_KEY"
    )


    indicators = {


        "inflation":
            "CPIAUCSL",


        "interest_rate":
            "FEDFUNDS",


        "unemployment":
            "UNRATE"

    }



    for name, series in indicators.items():


        url = (
            "https://api.stlouisfed.org/fred/"
            "series/observations"
        )


        params = {

            "series_id": series,

            "api_key": fred_key,

            "file_type":"json",

            "sort_order":"desc",

            "limit":1
        }



        response=requests.get(
            url,
            params=params
        )


        result=response.json()


        try:

            value=result[
                "observations"
            ][0]["value"]


            data[name]=float(value)


        except:


            data[name]=None



    return data