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
    url = common.get_url_from_xml('vote') + '?type=awardguestvote'
    print(url)
    configHttp.set_url(url)

    # 设置请求头
    cookie = voteInfo[i][2]
    print(cookie)
    # expert_userInfo = voteInfo[i][3]
    # print(expert_userInfo)
    header = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip', 'deflate'
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Connection': 'keep-alive',
    'Content-Length': '55',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'http://www.szzcs.com.cn',
    'Origin': 'http://www.szzcs.com.cn',
    'deflateAccept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Referer': 'http://www.szzcs.com.cn/m/topProjectInfo.aspx?pcode=W263',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': cookie
    }

    configHttp.set_headers(header)

    #设置body
    data = {"pid": 387, "ptype": 1, "vote": 'jTNB+MK1IBYOta+7CmyuUZpWJ1VTQUvd'}
    configHttp.set_data(data)

    #test Interface
    configHttp.post()

    # 等待时间
    w = random.randint(1, 3)
    time.sleep(w)








