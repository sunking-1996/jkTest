import pytest
import requests
import allure
from common.read_yml import readyml
import os

data = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))+r'\data\test_data.yml'
login_data = readyml(data)

@pytest.mark.web
@pytest.mark.parametrize("userAccount,userPwd,rcode,scode", login_data['login'])
@allure.feature("登录接口")
def test_loginfunc(userAccount,userPwd,rcode,scode):
    url = "http://www.fhd001.com/loginAccount.do"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                  "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                  "Referer":"http://www.fhd001.com/" }   # get方法其它加个ser-Agent就可以了
    body = {"userAccount":userAccount,
                "userPwd":userPwd
    } #参数存字典
    s = requests.session()
    request = s.post(url=url,data=body,headers=header)
    r   =  request.json()  #解析json
    #print("\n" + "返回的结果:%s" % r)

    ##实际结果
    assert r["rcode"] == rcode and r["scode"] == scode

if __name__ == '__main__':
    pytest.main(["-s","-v","test_jk_login.py"])