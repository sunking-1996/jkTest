import requests
import pytest

def test_querypack(login_fix):
    url = "https://saasapi.fhd001.com/api/package/queryPackage.do"
    body =  {"sort":"createTime",
             "desc":"true",
             "page":1,
             "pageSize":10,
             "status":0,
             "token":login_fix.cookies['fhd_token']
    } #参数存字典
    request = login_fix.post(url=url,data=body)
    r = request.json()  #解析json
    print("\n"+"接口返回值:%s" % r)

    ##实际结果
    assert r["rcode"] == 0 and r["scode"] == 0

if __name__ == "__main__":

     pytest.main(["-s","-v","test_fhdjk_queryPackage.py"])
