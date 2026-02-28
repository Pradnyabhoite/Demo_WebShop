import openpyxl

def read_excel(sheet):
    book = openpyxl.load_workbook("testdata/test_data.xlsx")
    data = book[sheet]
    rows = []
    for row in data.iter_rows(min_row=2, values_only=True):
        rows.append(row)
    return rows
