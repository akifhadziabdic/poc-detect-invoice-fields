# Copyright NovaHorizon

from services.chat_gpt_service import ChatGptService
from services.csv_export_service import CsvExportService
from services.pdf_service import PdfFields, PdfService


if __name__ == "__main__":
  pdf_reader = PdfService()
  chat_gpt = ChatGptService()
  csv_export = CsvExportService()

  pdf_text = pdf_reader.pdf_to_text()
  fields = chat_gpt.extract_fields([status.value for status in PdfFields], pdf_text)
  csv_export.export_data_to_csv_file(fields)