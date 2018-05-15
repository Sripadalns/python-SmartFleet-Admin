# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:37:09 2018

@author: sripals
Des: The main aim of this program is to parse the data available at School_info
This excel sheet have all the CBSE chennai school information.

After parsing data will be moved to school_data.xlsx. That will have a refined 
data

"""

from xlrd import open_workbook
import xlsxwriter

book = open_workbook( 'C:\Users\sripals\Desktop\school_info.xlsx')
sheet = book.sheet_by_index(0)

writebook = xlsxwriter.Workbook('C:\Users\sripals\Desktop\school_data.xlsx')
worksheet = writebook.add_worksheet('Sheet1')

 # Write some data headers.
worksheet.write('A1', 'S.Num')
worksheet.write('B1', 'School Name')
worksheet.write('C1', 'Prinicipal')
worksheet.write('D1', 'email')
worksheet.write('E1', 'Phone')
worksheet.write('F1', 'Location')
write_index = 0
# read header values into the list    
dict_list = []
for row_index in xrange(1, sheet.nrows):
    if(row_index%5 == 0):
        write_index = write_index +1
        s = str(sheet.cell(row_index-1,1)) # Read School Name
        c = str(sheet.cell(row_index-1,2)) # Read Phone Number
        p = str(sheet.cell(row_index,1)) # Read Prinicipal Name
        e = str(sheet.cell(row_index,2)) # Read email Information
        Sname= s[16:]
        Pname= p[27:]
        Contact = c[20:]
        email = e[17:]
        worksheet.write_string(write_index,1,Sname)
        worksheet.write_string(write_index,4,Contact)
        worksheet.write_string(write_index,2,Pname)
        worksheet.write_string(write_index,3,email)
        

