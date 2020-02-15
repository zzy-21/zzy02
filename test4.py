import requests,json
# urlstr='http://www.wanandroid.com/article/query?'
# payload={'k':'Android'}
#
# r =requests.get(url=urlstr,params=payload)
#
# print('以text的形式输出',r.text)
# print('以contet的形式输出',r.content)
# print('输出状态码',r.status_code)
# print('以headers的形式输出',r.headers)
# # print('以json的形式输出',r.json())
# print('以url的形式输出',r.url)
# print('以enconding的方式输出',r.encoding)
# print('以cookie的形式输出',r.cookies)
# print('以raw的形式输出',r.raw)
urlstr='https://www.wanandroid.com/user/login'
payload={'username':'zhaozhenyu','password':'zzy123456'}

paylod=json.dumps(payload)

r=requests.post(url=urlstr,data=payload)

# if r.status_code==200:
#     if r.json()['errorCode']== 0:
#         if r.json()['data']['username']=='zhaozhenyu':
#             print('登录成功')
# else:
#     print('登录失败')
# 导入requests包
# import requests
# # 发送请求
# urlstr='https://www.wanandroid.com/user/login'
# data={'username':'zhaozhenyu','password':'zzy123456'}
# s=requests.session()
#
# r=s.post(url=urlstr,data=data)
# r2=s.get('https://www.wanandroid.com/lg/todo/list/0')
# print('*****',r2.text)
# print('*******',r.text)

# urlstr='https://www.wanandroid.com/user/login'
# data={'username':'zhaozhenyu','password':'zzy123456'}
# s=requests.post(url=urlstr,data=data)
# print('****',s.text)
# print('*****',s.cookies)
# print('*****',s.headers)
# cookie=s.cookies
# r2=requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)
# print('***',r2.text,r2.status_code)

urlstr='https://www.wanandroid.com/user/login'
data={'username':'zhaozhenyu','password':'zzy123456'}
s=requests.post(url=urlstr,data=data)
# print('****',s.text)
# print('*****',s.cookies['JSESSIONID'])
# print('*****',s.headers)
# cookie={
#     'JSESSIONID':r.cookies['JSESSIONID']
# }
header={
    'cookie':'JSESSIONID'+ r.cookies['JSESSIONID']
}
r2=requests.get('https://www.wanandroid.com/lg/todo/list/0',headers=header)
print('***',r2.text,r2.headers)
result=r2.text.find('已完成清单')
print(result)
if result!=-1:
    print('查询成功')
else:
    print('查询失败')




