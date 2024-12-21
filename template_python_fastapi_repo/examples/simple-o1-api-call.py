# template_python_fastapi_repo/examples/simple-o1-api-call.py
# https://platform.openai.com/docs/guides/reasoning

from openai import OpenAI
from template_python_fastapi_repo.settings import Settings
from template_python_fastapi_repo.helpers.logger_helper import get_logger

# Get the configured logger
logger = get_logger()

settings = Settings()

client = OpenAI(api_key=settings.OPENAI_API_KEY)

prompt = """
Write a bash script that takes a matrix represented as a string with
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.chat.completions.create(
    model="o1-mini", messages=[{"role": "user", "content": prompt}]
)

print("This may take a few seconds...")
print(response.choices[0].message.content)