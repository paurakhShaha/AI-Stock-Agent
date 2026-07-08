import json

from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class InvestmentCommitteeAgent:


    def __init__(self):

        self.name="investment_committee"


        with open(
            "prompts/committee_prompt.txt",
            encoding="utf-8"
        ) as f:

            self.system_prompt=f.read()



    def analyze(
        self,
        ticker,
        reports
    ):


        prompt=f"""

{self.system_prompt}


Stock:

{ticker}


Analyst Reports:

{json.dumps(
    reports,
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

            decision=json.loads(
                response.text
            )


        except:


            decision={

                "decision":
                    "HOLD",

                "confidence":
                    0,

                "reasoning":
                    "Invalid AI response"

            }



        return {


            "agent":
                self.name,


            "ticker":
                ticker,


            "decision":
                decision,


            "tokens":{


                "input":
                response
                .usage_metadata
                .prompt_token_count,


                "output":
                response
                .usage_metadata
                .candidates_token_count

            }

        }