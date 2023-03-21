# coding:utf-8
from distutils import version
import requests
import urllib3
import pytest
import re
urllib3.disable_warnings()  # 忽略警告
@pytest.fixture()
class Login():
    def __init__(self, s):
        self.s = s
    def test_login(self):
        '''用例描述: 登录接口，正确入参'''
        url = "https://www.fhd001.com/loginAccount.do"
        body = {
        "userAccount": "15167168967",
        "userPwd": "123456"
        }
        r = self.s.post(url, data=body,verify=False)
        print("\n"+"返回的结果:%s" % r.text)
        # 实际结果
        result_rcode = r.json().get("rcode")
        result_scode = r.json().get("scode")
        # 期望结果 "rcode":0,"scode":"0"
        assert result_rcode == 0
        assert result_scode == 0

if __name__ == '__main__':
    s = requests.session()
    a = Login(s)  # 实例化
    a.test_login()    # 登陆

