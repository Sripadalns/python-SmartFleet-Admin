from email_send import send_email
import time

import xlrd
 
book = xlrd.open_workbook('Send_List.xlsx')
 
# get the first worksheet
first_sheet = book.sheet_by_index(0)
 
# read a row
print first_sheet.row_values(0)
 
# read a cell
cell = first_sheet.cell(0,0)
print cell
print cell.value

for row in range(first_sheet.nrows):
    School_Name = first_sheet.cell(row,0)
    print School_Name.value
    School_Email = first_sheet.cell(row,1)
    print School_Email.value
    send_email( School_Email.value, School_Name.value )
    time.sleep(30)
