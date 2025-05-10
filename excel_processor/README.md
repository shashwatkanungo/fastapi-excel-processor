#  FastAPI Excel Processor

##  Description

This FastAPI app processes an Excel file and provides the following endpoints:

- `GET /list_tables`: Lists all sheet names.
- `GET /get_table_details`: Returns row names (first column) from the specified sheet.
- `GET /row_sum`: Returns the sum of numeric values in the specified row.

##  How to Run

```bash
pip install fastapi uvicorn xlrd
uvicorn app.main:app --host 0.0.0.0 --port 9090 --reload
