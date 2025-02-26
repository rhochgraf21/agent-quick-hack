# @author: Aparnaa Senthilnathan, Bertan Berker, Anshul Kiyawat, Paras Jain
# ----

import os
import dotenv
from openai import OpenAI

key = os.getenv("OPENAI_KEY")

model  = OpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
