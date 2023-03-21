import pytest
import requests
from common.read_yml import readyml
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
a = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data.yml")
print(a)
test_data = readyml(a)
print(test_data['test_data'])
# test_data = [
#     ("M", {"message": "update some data!", "code": 0}),
#     ("F", {"message": "update some data!", "code": 0}),
# ]
@pytest.mark.parametrize("userAccount,userPwd,rcode,scode", test_data['login'])
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
    print("\n" + "返回的结果:%s" % r.text)

    ##实际结果
    assert r["rcode"] == rcode and r["scode"] == scode

if __name__ == '__main__':
    pytest.main(["-s", "test_jk_login.py"])