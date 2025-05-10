from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.excel_utils import load_excel, get_sheet_names, get_row_names, get_row_sum

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

EXCEL_PATH = "Data/capbudg.xls"

@app.get("/list_tables")
def list_tables():
    try:
        workbook = load_excel(EXCEL_PATH)
        tables = get_sheet_names(workbook)
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(..., description="Name of the table/sheet")):
    try:
        workbook = load_excel(EXCEL_PATH)
        row_names = get_row_names(workbook, table_name)
        return {
            "table_name": table_name,
            "row_names": row_names
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/row_sum")
def row_sum(
    table_name: str = Query(..., description="Name of the table"),
    row_name: str = Query(..., description="Row name (first column value)")
):
    try:
        workbook = load_excel(EXCEL_PATH)
        total = get_row_sum(workbook, table_name, row_name)
        return {
            "table_name": table_name,
            "row_name": row_name,
            "sum": total
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
