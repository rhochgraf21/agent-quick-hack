import openai
import sqlite3
import os
from dotenv import load_dotenv

# Define base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Set OpenAI API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Set database path
DB_PATH = os.path.join(BASE_DIR, "..", "db_test.sqlite")  # Adjust based on the DB you want

# TODO remove this as open ai api team is making their one method
def query_openai(prompt):
    """ Calls OpenAI API with a given prompt and returns the response. """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()


def execute_sql(query):
    """ Executes an SQL query against the database and returns the results. """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.commit()
        return results
    except Exception as e:
        return f"SQL Error: {e}"
    finally:
        conn.close()


def process_natural_language_query(nl_query):
    """
    1. Converts natural language to SQL
    2. Executes SQL query
    3. Calls OpenAI for post-processing
    4. Returns processed HTML output
    """
    sql_prompt = f"Convert this natural language query into SQL: {nl_query}"
    sql_query = query_openai(sql_prompt)

    sql_results = execute_sql(sql_query)

    post_processor_prompt = f"Given the SQL results {sql_results}, generate an HTML table."
    html_output = query_openai(post_processor_prompt)

    return html_output
