# @author: Aparnaa Senthilnathan and Bertan Berker
# ----

import os
import dotenv
import OpenAI

load_dotenv()
OPENAI_API_KEY = ""
key = os.getenv("OPENAI_KEY")

model  = ChatOpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
