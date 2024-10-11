# Copyright NovaHorizon

import openai

from openai import OpenAI
from config.config import Config


class ChatGptService:
  _client = OpenAI()
  _prompt = """
    I will provide content of the pdf file and fields you should extract from the pdf.
    Generate json result without any other characters and without formatting like ```json.
    Keys will be fields and values will be found data in the file.
    Keys that starts with items should be generated as list of the items with key items.
  """

  def __init__(self):
    openai.api_key = Config.chat_gpt_api_key

  def extract_fields(self, fields, content):
    response = self._client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
          "role": "user", 
          "content": f"${self._prompt} fields: `${fields}` content: `${content}`"
        }],
    )
    return response.choices[0].message.content