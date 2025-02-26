# @author: Aparnaa Senthilnathan, Bertan Berker, Anshul Kiyawat, Paras Jain
# ----

import os
import dotenv
from openai import OpenAI

key = os.getenv("OPENAI_KEY")

model  = OpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])


# from pydantic import BaseModel
# from openai import OpenAI

# client = OpenAI()

# class Step(BaseModel):
#     explanation: str
#     output: str

# class MathReasoning(BaseModel):
#     steps: list[Step]
#     final_answer: str

# completion = client.beta.chat.completions.parse(
#     model="gpt-4o-2024-08-06",
#     messages=[
#         {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
#         {"role": "user", "content": "how can I solve 8x + 7 = -23"}
#     ],
#     response_format=MathReasoning,
# )

# math_reasoning = completion.choices[0].message.parsed