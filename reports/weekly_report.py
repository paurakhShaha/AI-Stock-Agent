import json
from datetime import datetime



def create_weekly_report(results):


    filename = (
        f"weekly_report_"
        f"{datetime.now().date()}.json"
    )


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(

            results,

            f,

            indent=4

        )


    return filename