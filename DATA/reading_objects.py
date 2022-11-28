# import xlrd
# from LIBRARY.config import Config
#
#
# class ReadExcel:
#
#     def read_test_data(self, sheetname):
#         wb = xlrd.open_workbook(Config.DATA_PATH)
#         ws = wb.sheet_by_name(sheetname)
#         columns = ws.ncols
#         rows = ws.get_rows()  #generator object
#         header = next(rows)
#         data = []
#
#         for row in rows:
#             values = ()
#             for j in range(columns):
#                 values += (row[j].value,)
#             data.append(values)
#         return data
#
#     def read_locator(self, sheetname):
#         wb = xlrd.open_workbook(Config.LOCATOR_PATH)
#         ws = wb.sheet_by_name(sheetname)
#         rows=ws.nrows
#         print(rows)
#         d={}
#         for i in range(1,rows):
#             rows=ws.row_values(i)
#             print(rows)
#             d[rows[0]]=(rows[1],rows[2])
#         return d
#     print(read_locator)

import xlrd
from LIBRARY.config import Config
#path = r'C:\Users\HP\Desktop\pythonProject1\MakeMyTrip\sprint2.xlsx'
#path=r"C:\Users\Sravani\Desktop\redbus_data.xlsx"
class ReadExcel:

    def read_test_data(self,data1):
        wb = xlrd.open_workbook(Config.DATA_PATH)
        ws = wb.sheet_by_name("data1")
        columns = ws.ncols
        rows = ws.get_rows()  #generator object
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data
    def read_locators(self,register12):
       wb= xlrd.open_workbook(Config.LOCATOR_PATH)
       ws = wb.sheet_by_name("register12")
       #rows = ws.get_rows()
       rows=ws.nrows

       #print(rows)
       #header = next(rows)
       d = {}
       # for row in rows:
       #  d[row[0].value] = (row[1].value,row[2].value)
       #  return d
       for i in range(1,rows):
           rows=ws.row_values(i)
           d[rows[0]]=(rows[1],rows[2])
       return d
# r=ReadExcel
# data=r.read_locators("register12")
# print(data)


















# #from LIBRARY.config import Config
# import xlrd
# from LIBRARY.config import Config
# #path= r"C:\Users\manch\Desktop\redbus_sign_in.xlsx"
#
# def read_locators():
#     workbook=xlrd.open_workbook(Config.DATA_PATH)
#     worksheet=workbook.sheet_by_name("reg_signin")
#     rows=worksheet.nrows
#     d={}
#     for i in range(1,rows):
#         row=worksheet.row_values(i)
#         print(row)
#         d[row[0]]=(row[1],row[2])
#     return d
# print(read_locators())