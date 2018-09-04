# -*- coding:utf-8 -*-
import sys
import util.ReadConfig
import script.truck.sendSmsCodeImp
import json

rc= util.ReadConfig.ReadConfig()
def runTruckCase(arr):
    resu=[]
    for i in range(0,len(arr)):
        interface_name = arr[i][3].split('/')[-1]
        module_name = arr[i][1].split('/')[-1]
        expect_code= arr[i][4]
        url=rc.get_TruckApiTestBaseUrl()+arr[i][3]
        id=int(arr[i][0])
        if interface_name == 'sendSmsCode':
            if module_name=='登录'.decode('utf-8'):
                rep=script.truck.sendSmsCodeImp.sendLoginCode(url)
            elif module_name=='注册'.decode('utf-8'):
                rep=script.truck.sendSmsCodeImp.sendRegCode(url)
            elif module_name=='忘记密码'.decode('utf-8'):
                rep=script.truck.sendSmsCodeImp.sendModPWDCode(url)
            else:
                sys.exit(0)

            respcode = json.loads(rep)['code']
            respmsg = json.loads(rep)['msg']
            rowresu=[id,expect_code,respcode,respmsg]
            resu.append(rowresu)
        else:
            print "no interface found!"
    return resu




