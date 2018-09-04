# -*- coding:utf-8 -*-
import xlrd,xlwt
from xlrd import open_workbook
from xlutils.copy import copy
def save_result(case_path,filename,arr):
    rb = open_workbook(case_path+filename)
    wb = copy(rb)
    ws=wb.get_sheet(0)
    for i in range(0, len(arr)):
        id=arr[i][0]
        expcode = arr[i][1]
        rescode=arr[i][2]
        resmsg=arr[i][3]
        if rescode == expcode :
            result='pass'
        else:
            result='fail'
        ws.write(id,5,rescode)
        ws.write(id,6,resmsg)
        ws.write(id,7,result)
    wb.save(case_path+filename)
