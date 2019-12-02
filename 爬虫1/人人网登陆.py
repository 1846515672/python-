import requests


#登陆接口查找
url = 'http://www.renren.com/PLogin.do'
#找form表单提交的参数
data = {"email":'15282771516', 'password':'xujin1846515672'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
#请求
response = requests.post(url=url, data=data, headers=headers).content.decode('utf-8')
with open('renrenwang.html', 'w', encoding='utf-8')as fp:
    fp.write(response)