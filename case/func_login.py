import requests

def login(s):
    '''登录获取token'''
    url = "https://www.fhd001.com/loginAccount.do"
    body = {
        "userAccount": "15167168967",
        "userPwd": "123456"
    }

    # token
    r = s.post(url, data=body,verify=False)

    token = r.cookies['fhd_token']
    print("取出token:%s" % token)

    h = {
        "Authorization": "Token %s" % token
    }
    s.headers.update(h)  # 更新到session会话
    # 更新之后的头部
    # print(s.headers)
    return token

if __name__ == '__main__':
    s = requests.session()   # s单独拿出来
    token = login(s)   # 登录

