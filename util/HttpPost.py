# -*- coding:utf-8 -*-
import requests

def httpPost(url,data):
    user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
    headers={'User-Agent':user_agent}
    response=requests.post(url,data=data,headers=headers)
    return response.text