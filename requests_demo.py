# requests 让代码实现网络请求

import requests

r = requests.get('https://smartgemchat.site/', timeout = 2.5) 
# 设置超时时间为2.5秒

# print(r.json()) # 报错
print(r.content)
print(r.url)
print(r.headers)
print(r.encoding)
print(r.cookies)

r2 = requests.post('https://smartgemchat.site/api/register', json={
  "username": "User002",
  "password": "123456"
})
print(r2.status_code)
print(r2.text)
print(r2.json())