# Copyright NovaHorizon

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  invoice_file = "data/invoice.pdf"
  chat_gpt_url = "https://api.openai.com"
  chat_gpt_files_path = "/v1/files"
  chat_gpt_api_key = os.environ.get('OPENAI_API_KEY', ValueError("Required value"))
  csv_output_path = "."