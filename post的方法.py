# import requests ,json
# # # 发送post请求
# urlstr ='https://www.wanandroid.com/user/login'
#
# payload={'username':'zhaozhenyu','password':'zzy123456'}
#
#  payload=json.dumps(payload)
#
# r=requests.post(url=urlstr,data=payload)
# # print(r.text)
# print(r.content)


# import requests,json
# urlstr ='https://www.wanandroid.com/user/login'
#
# payload={'username':'zhaozhenyu','password':'zzy123456'}
#
# r=requests.post(url=urlstr,data=payload)
# print(r.status_code)
# if r.status_code==200:
#     if r.json()['errorCode']==0:
#         if r.json()['']!=:
#             print('登录成功')
#         else:
#             print('登录失败')



# import requests
# # 发送post请求
# urlstr ='https://www.wanandroid.com/user/login'
# data={'username':'zhaozhenyu','password':'zzy123456'}
#
# # 初始化session对象
# s=requests.session()
#
# # 2--通过session对象发送请求，服务器设置在本地的cookie会保存在本地
# r=s.post(url=urlstr,data=data)
# #
# r2=s.get('https://www.wanandroid.com/lg/todo/list/0')
# print(r2.text)
# print(r.text)
#
# import requests
#
# urlstr ='https://www.wanandroid.com/user/login'
# data={'username':'zhaozhenyu','password':'zzy123456'}
# r=requests.post(url=urlstr,data=data)
# print('text方法',r.text)
# print('cookies方法',r.cookies)
# print('headers方法',r.headers)
#
# cookie=r.cookies
#
# r2=requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)
# print('携带cookie发送请求',r2.text,r2.status_code)



# import requests
#
# urlstr ='https://www.wanandroid.com/user/login'
#
# data={'username':'zhaozhenyu','password':'zzy123456'}
#
# r=requests.post(url=urlstr,data=data)
#
# print('text方法',r.text)
# print('cookies方法1',r.cookies['JSESSIONID'])
# print('cookies方法2',r.cookies)
# cookie={
#     'JSESSIONID':r.cookies['JSESSIONID']
#
# }
# r2=requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)
# print('******',r2.text)
# print('headers的',r2.headers)


import requests,re

urlstr ='https://www.wanandroid.com/user/login'

data={'username':'zhaozhenyu','password':'zzy123456'}

r=requests.post(url=urlstr,data=data)

print('text方法',r.text)
print('cookies方法1',r.cookies['JSESSIONID'])
print('cookies方法2',r.cookies)
header={
    'cookie':'JSESSIONID'+r.cookies['JSESSIONID']
}
r2=requests.get('https://www.wanandroid.com/lg/todo/list/0',headers=header)
print('******',r2.text)
print('headers的',r2.headers)
result=r2.text.find('已完成清单')
print(result)
if result !=-1:
    print('查询成功')
else:
    print('查询失败')
pattern=re.compile(r';\">(.*?)<\/h2')
result=pattern.findall(r.text)
print(result)









