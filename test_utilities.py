import openpyxl as openpyxl
from selenium.common.exceptions import NoSuchElementException


def test_dynamicparameter(value):
    try:
        s = value + 1
        return s
    except "NoSuchElementsExcemption":
        print()


def Write_data(file, sheetname, row, column, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    sheet.cell(row, column).value = data
    workbook.save(file)


