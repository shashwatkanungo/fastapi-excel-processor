import xlrd

def load_excel(file_path):
    return xlrd.open_workbook(file_path)

def get_sheet_names(workbook):
    return workbook.sheet_names()

def get_row_names(workbook, sheet_name):
    if sheet_name not in workbook.sheet_names():
        raise ValueError(f"Sheet '{sheet_name}' not found in the Excel file.")
    sheet = workbook.sheet_by_name(sheet_name)
    row_names = [str(sheet.cell_value(rowx, 0)).strip() for rowx in range(sheet.nrows)]
    return [r for r in row_names if r]

def get_row_sum(workbook, sheet_name, row_name):
    if sheet_name not in workbook.sheet_names():
        raise ValueError(f"Sheet '{sheet_name}' not found.")
    sheet = workbook.sheet_by_name(sheet_name)

    for rowx in range(sheet.nrows):
        first_col = str(sheet.cell_value(rowx, 0)).strip()
        if first_col == row_name:
            values = sheet.row_values(rowx)[1:]  # Skip first column
            numeric_sum = sum(
                float(val) for val in values if isinstance(val, (int, float))
            )
            return numeric_sum
    raise ValueError(f"Row name '{row_name}' not found in table '{sheet_name}'.")
