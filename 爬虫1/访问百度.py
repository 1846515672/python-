import requests

#1路由url
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%9F%A5%E4%B9%8E&rsv_pq=87b260740002ce7d&rsv_t=9be22oIIohMwdxbrbTlTgCl%2F2bHXQfP8eGizkJUohKPE0prmFFBabkgQbek&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=8&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&inputT=2883&rsv_sug4=8621"

#2请求方式Request Method:GET

#2.1做伪装,添加headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

#3发起请求
response = requests.get(url=url, headers=headers)
print(response)

#4查看响应内容
    # respons.text:返回文本信息
# print(response.text)
    # response.content:返回字节流信息,  +.decode("gbk")
# print(response.content.decode("utf-8"))

#5写入本地文件
with open('baidu.html', "w", encoding='utf-8')as fp:
    fp.write(response.content.decode('utf-8'))
print(response.content.decode('utf-8'))