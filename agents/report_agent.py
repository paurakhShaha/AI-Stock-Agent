import json

from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



class ReportGeneratorAgent:


    def __init__(self):

        self.name="report_generator"


        with open(
            "prompts/report_prompt.txt",
            encoding="utf-8"
        ) as f:

            self.system_prompt=f.read()



    def generate(
        self,
        ticker,
        analysis
    ):


        prompt=f"""

{self.system_prompt}


Company:

{ticker}


Analysis:

{json.dumps(
    analysis,
    indent=2
)}

"""


        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                response_mime_type=
                "application/json"

            )

        )


        try:

            report=json.loads(
                response.text
            )


        except:


            report={

                "title":
                "Analysis Report",

                "summary":
                "Generation failed"

            }



        return {


            "agent":
            self.name,


            "ticker":
            ticker,


            "report":
            report,


            "metadata":{

                "tokens":
                response
                .usage_metadata
                .total_token_count

            }

        }