# Copyright NovaHorizon

from enum import Enum
import pytesseract

from pdf2image import convert_from_path
from config.config import Config

class PdfFields(Enum):
  bill_to = "bill_to"
  ship_to = "ship_to"
  invoice_no_date = "invoice_no_date"
  sales_order_no_date = "sales_order_no_date"
  customer_vat_no = "customer_vat_no"
  name = "items.name"
  quantity = "items.quantity"
  currency = "items.currency"
  unit_price = "items.unit_price"
  totals = "totals"
  
class PdfService:

  _fields = []

  def pdf_to_text(self, invoice_file = Config.invoice_file):
    text = ""
    pages = convert_from_path(invoice_file, dpi=200)
    for page in pages:
      text = text + pytesseract.image_to_string(page)
    return text
