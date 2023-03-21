import requests
import pytest
from urllib import parse
from test_case.conftest import test_data
from common.read import get_cookies,get_headers


@allure.story("---分页查询包裹用例---")
@pytest.mark.parametrize("sort,desc,page,pageSize,status,rcode,scode",test_data["queryPackages"])
def test_querypack(sort,desc,page,pageSize,status,rcode,scode):
    s = get_headers()
    #decode解码
    fhd_token=parse.unquote(get_cookies()[1])
    url = "http://typapi.fhd001.com/api/package/queryPackage.do"
    body =  {"sort":sort,
             "desc":desc,
             "page":page,
             "pageSize":pageSize,
             "status":status,
             "token":fhd_token
    } #参数存字典
    s = requests.session()
    request = s.post(url=url,data=body)
    r   =  request.json()  #解析json
    print(r)

    ##实际结果
    assert r["rcode"] == rcode and r["scode"] == scode

if __name__ == "__main__":

     pytest.main(["-s","-v","test_fhdjk_queryPackage.py"])
