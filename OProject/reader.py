import openpyxl
from openpyxl import Workbook, load_workbook

book = load_workbook("karbon_ayakizi.xlsm")
sheet = book.active
max_row = 630
number = 2
a = "{sutun}{number}"

rows = []
each_row = []


a.format(sutun='B', number=number)
for i in range(max_row):
    b = sheet[a.format(sutun='B', number=i+1)].value
    c = sheet[a.format(sutun='C', number=i+1)].value
    d = sheet[a.format(sutun='D', number=i+1)].value
    e = sheet[a.format(sutun='E', number=i+1)].value
    f = sheet[a.format(sutun='F', number=i+1)].value
    g = sheet[a.format(sutun='G', number=i+1)].value
    h = sheet[a.format(sutun='H', number=i+1)].value
    i = sheet[a.format(sutun='I', number=i+1)].value

    each_row = [b,c,d,e,f,g,h,i]
    rows.append(each_row)
print(rows)
