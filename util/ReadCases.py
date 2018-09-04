# -*- coding:utf-8 -*-
import xlrd
import sys
import util.ReadConfig

def ReadCases(CaseFilename):
    cls=[]
    rd = util.ReadConfig.ReadConfig()
    CaseFile = rd.get_TruckCasePath()+CaseFilename
    try:
        fd = open(CaseFile)
    except IOError:
        print "File is not accessible."
        sys.exit(1)
    fd.close()
    xd = xlrd.open_workbook(CaseFile)
    table = xd.sheets()[0]
    nrows=table.nrows
    for i in range(nrows):
        if table.row_values(i)[8] =='是'.decode('utf-8'):
            cls.append(table.row_values(i))
    return cls
if __name__=='__main__':
    ReadCases('测试20180518.xlsx'.decode('utf-8'))