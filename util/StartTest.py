# -*- coding:utf-8 -*-
import sys
import ReadCases
import RunCases
import ReadConfig
import SaveResult
import log.InterfaceTestLog
import ExcelParse

arr1=[]
caseFileName='测试20180518.xlsx'.decode('utf-8')
htmlfile='test1.html'
rc = ReadConfig.ReadConfig()
casePath=rc.get_TruckCasePath()
cls=[]
cls=ReadCases.ReadCases(caseFileName)
arr1=RunCases.runTruckCase(cls)
SaveResult.save_result(casePath,caseFileName,arr1)
log.InterfaceTestLog.logging.info('验证码获取测试')
#ExcelParse.excelParse(casePath+caseFileName,casePath+htmlfile)
