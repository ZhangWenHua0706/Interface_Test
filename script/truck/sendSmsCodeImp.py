# -*- coding:utf-8 -*-

import util.ReadConfig
import util.HttpPost
import model.sendSmsCode
import json

ms = model.sendSmsCode.sendSmsCode()
rc = util.ReadConfig.ReadConfig()
casepath = rc.get_TruckCasePath()
def sendLoginCode(url):
    ms.setLoginCodeType()
    data={'mobile':ms.mobile,'codeType':ms.getLoginCodeType()}
    return util.HttpPost.httpPost(url,data)
def sendRegCode(url):
    ms.setRegCodeType()
    data={'mobile':ms.mobile,'codeType':ms.getRegCodeType()}
    return util.HttpPost.httpPost(url,data)
def sendModPWDCode(url):
    ms.setModPWDCodeType()
    data={'mobile':ms.mobile,'codeType':ms.getModPWDCodeType()}
    return util.HttpPost.httpPost(url,data)