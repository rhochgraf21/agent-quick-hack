# @author: Aparnaa Senthilnathan and Bertan Berker
# ----

import os
import dotenv
from openai import OpenAI

OPENAI_API_KEY = ""
key = os.getenv("OPENAI_KEY")

model  = OpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
