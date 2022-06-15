"""
Implemented use cases with dependencies injected

https://proofit404.github.io/dependencies/
"""
import typer
from dependencies import Injector

from adapters import spreadsheet_adapter
from usecases import convert_data
from services import google_sheets, geocoding, translation, address_sanitizer
from repositories import csv
from config import settings
from validation import error_collector, composite_validator, RequiredFieldsValidator, CategoriesValidator


class ConvertSpreadsheetData(Injector):
    usecase = convert_data.ConvertSpreadsheetData
    settings = settings.Settings(_env_file="config/.env.example")
    log = print
    spreadsheet_reader = google_sheets.GoogleSheetsReader
    adapter = spreadsheet_adapter.SpreadsheetAdapter
    address_sanitizer = address_sanitizer.AddressSanitizer
    geocoder = geocoding.GeoCodingProcessor
    translator = translation.PointTranslator
    error_collector = error_collector.ErrorCollector
    validator = composite_validator.CompositeValidator
    validators = [RequiredFieldsValidator(), CategoriesValidator()]
    csv_repository = csv.CSVRepository


class ConvertSpreadsheetDataLocally(ConvertSpreadsheetData):
    settings = settings.Settings(_env_file="config/.env")
