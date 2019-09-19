import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
import time
import random

addGroupManager = common.get_xls("vote.xls","vote")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()

@paramunittest.parametrized(*addGroupManager)
class Vote(unittest.TestCase):
    def setParameters(self, case_name, method, cookie, userInfo, pid, ptype, vote, msg):
        '''

        :param case_name:
        :param method:
        :param cookie:
        :param userInfo:
        :param pid:
        :param ptype:
        :param vote:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.cookie = str(cookie)
        self.expert_userInfo = str(userInfo)
        self.pid = str(pid)
        self.ptype = str(ptype)
        self.vote = str(vote)
        self.msg = str(msg)

    def description(self):
        """
                test report description
                :return:
                """
        return  self.case_name

    def setUp(self):
        """

                :return:
                """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        # self.cookie = 'JSESSIONID=111373CF525F2CC5FAF1D64A4348837C'

    def testVote(self):
        '''
        set url
        :return:
        '''
        self.url = common.get_url_from_xml('vote')
        print(self.url)
        configHttp.set_url(self.url)

        #set headers
        cookie = str(self.cookie)
        header = {"Cookie":cookie ,"expert_userInfo":self.expert_userInfo}
        configHttp.set_headers(header)


        #set data
        data = {"pid": self.pid, "ptype": self.ptype, "vote": self.vote }
        configHttp.set_data(data)
        print('第三步：设置发送请求的参数')

        #test interface
        self.return_json = configHttp.post()
        self.url = self.return_json.url
        method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法：" + method)

        #等待时间
        time.sleep(random.randint(4,12))


    def tearDown(self):
        """

        :return:
        """
        # self.log.build_case_line(self.case_name)
        print("测试结束，输出log完结\n\n")


if __name__ == '__main__':
    Vote(unittest.TestCase)