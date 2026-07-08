import json

from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class DevilAgent:


    def __init__(self):

        self.name="devil_agent"


        with open(
            "prompts/devil_prompt.txt",
            encoding="utf-8"
        ) as f:

            self.system_prompt=f.read()



    def analyze(
            self,
            ticker,
            analysis_data
    ):



        prompt=f"""

{self.system_prompt}


Stock:

{ticker}


Analysis Data:

{json.dumps(
    analysis_data,
    indent=2
)}

"""



        response=client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                response_mime_type=
                "application/json"

            )

        )



        try:

            result=json.loads(
                response.text
            )


        except:


            result={

                "bear_case":
                    [
                    "Invalid AI response"
                    ],

                "major_risks":[],

                "failure_probability":50,

                "summary":
                    "Unable to analyze"

            }



        return {


            "agent":
                self.name,


            "ticker":
                ticker,


            "analysis":
                result,


            "confidence":

                response
                .usage_metadata
                .total_token_count

        }