import requests
import pytest
import allure
from common.read_yml import readyml
import os

data = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))+r'\data\test_data.yml'
queryPackages_data = readyml(data)

@pytest.mark.web
@pytest.mark.parametrize("sort,desc,page,pageSize,status,rcode,scode", queryPackages_data['queryPackages'])
@allure.feature("查询包裹接口")
def test_querypack(login_fix,sort,desc,page,pageSize,status,rcode,scode):
    url = "https://saasapi.fhd001.com/api/package/queryPackage.do"
    body =  {"sort":sort,
             "desc":desc,
             "page":page,
             "pageSize":pageSize,
             "status":status,
             "token":login_fix.cookies['fhd_token']
    } #参数存字典
    request = login_fix.post(url=url,data=body)
    r = request.json()  #解析json
    #print("\n"+"接口返回值:%s" % r)

    ##实际结果
    assert r["rcode"] == rcode and r["scode"] == scode

if __name__ == "__main__":

    pytest.main("-s","-v",["test_fhdjk_queryPackage.py"])
