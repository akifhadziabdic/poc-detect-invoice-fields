# Copyright NovaHorizon

import re
import os
import csv
import json

from config.config import Config
from datetime import datetime

from services.pdf_service import PdfFields
  
def generate_file_name():
  now = datetime.now()
  formatted_date = now.strftime('%Y-%m-%d_%H-%M-%S')
  return f'output_{formatted_date}.csv'

def generate_headers():
  return ["id"] + [status.value.replace("items.", "") for status in PdfFields]


class CsvExportService:

  def export_data_to_csv_file(self, json_fields):
    fields = json.loads(json_fields)
    items = fields.get("items")
    data = list(map(lambda item: self._to_row(item, items, fields), items))
    self._save_file(data)

  def _to_row(self, item, items, fields):
    row = [
      items.index(item),
      fields.get(PdfFields.bill_to.value),
      fields.get(PdfFields.ship_to.value),
      fields.get(PdfFields.invoice_no_date.value),
      fields.get(PdfFields.sales_order_no_date.value),
      fields.get(PdfFields.customer_vat_no.value),
      item.get(PdfFields.name.value[6:]),
      item.get(PdfFields.quantity.value[6:]),
      item.get(PdfFields.currency.value[6:]),
      item.get(PdfFields.unit_price.value[6:]),
      fields.get(PdfFields.totals.value).split()[-1],
    ]
    return list(map(lambda field: re.sub(r'\s+', ' ', f"{field}"), row))

  def _save_file(self, data, headers = generate_headers(), file_name = generate_file_name(), path = Config.csv_output_path):
    with open(os.path.join(path, file_name), mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(headers)
      writer.writerows(data)