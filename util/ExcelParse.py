# -*- coding:utf-8 -*-
import pandas as pd
import codecs

def excelParse(excelfile,htmlfile):
    xd = pd.ExcelFile(excelfile)
    df = xd.parse()
    with codecs.open(htmlfile,'w','utf-8') as html_file:
        html_file.write(df.to_html(header = True,index = False))