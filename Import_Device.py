# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:32:52 2018

@author: sripals
"""

import xlrd
from Device_Add import login
from Device_Add import add_device
import time




def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
    cookie = login()
 
    # print number of sheets
    #print book.nsheets
 
    # print sheet names
    #print book.sheet_names()
 
    # get the first worksheet
    sheet = book.sheet_by_index(0)
 
    # read a row
   # print sheet.row_values(0)
   # read a cell
    for i in xrange(sheet.nrows):
        if i+1 < sheet.nrows :
            devID = sheet.cell(i+1,1)
            name  = sheet.cell(i+1,3)
            print str(name)
            add_device(cookie,str(name.value),int(devID.value))
            time.sleep(150)
            
        #print cell

   # add_device(cookie,str(name.value),int(devID.value))
    # read a row slice
    #add_device(cookie,str(name.value),int(devID.value))
    print sheet.row_slice(rowx=0,
                          start_colx=0,
                          end_colx=2)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    path = "Device_Info.xlsx"
    
    open_file(path)
    #add_device(cookie,str('samp'),int(382067))
