# @author: Aparnaa Senthilnathan and Bertan Berker
# ----

import os
import dotenv

dotenv.load_dotenv()
OPENAI_API_KEY = ""

model  = OpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
