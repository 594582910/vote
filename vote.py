import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
import time
import random


localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
voteInfo = common.get_xls("vote.xls","vote")
# print(voteInfo)
L = len(voteInfo)




for i in range(L):

    #设置url
    url = common.get_url_from_xml('vote')
    configHttp.set_url(url)

    # 设置请求头
    cookie = voteInfo[i][2]
    expert_userInfo = voteInfo[i][3]
    print(expert_userInfo)
    header = {"Cookie":cookie ,"expert_userInfo":expert_userInfo }
    configHttp.set_headers(header)

    #设置body
    data = {"pid": 378, "ptype": 1, "vote": 'jTNB+MK1IBYOta+7CmyuUZpWJ1VTQUvd'}
    configHttp.set_data(data)

    #test Interface
    configHttp.post()

    # 等待时间
    w = random.randint(1, 3)
    time.sleep(w)








