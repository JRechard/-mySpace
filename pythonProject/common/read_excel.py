import os
from common import get_project_path
from xlrd import open_workbook

project_path = get_project_path.get_path()


class ReadExcel:
    def __init__(self):
        pass

    def get_xls(self, xls_name, sheet_name):
        cls = []
        xls_path = os.path.join(project_path, 'testFiles', 'case', xls_name)
        file = open_workbook(xls_path)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != "case_name":
                cls.append(sheet.row_values(i))
        return cls
