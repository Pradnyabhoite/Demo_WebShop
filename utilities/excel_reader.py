from openpyxl import load_workbook

class ExcelReader:
    def __init__(self, file_path, sheet_name):
        self.workbook = load_workbook(file_path)
        self.sheet = self.workbook[sheet_name]

    def get_data(self):
        data = []
        rows = list(self.sheet.rows)

        headers = [cell.value.strip().lower() for cell in rows[0]]
        for row in rows[1:]:
            row_data = {}
            for key, cell in zip(headers, row):
                row_data[key] = cell.value
            data.append(row_data)
        return data

