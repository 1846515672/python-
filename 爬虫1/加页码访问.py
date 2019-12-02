import requests

# kw = input('请输入查找名称:')
# url = 'http://tieba.baidu.com/f?kw={}&fr=ala0&tpl=5'.format(kw)
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
#
# for page in range(10):
#     full_url = url + str(page*50)
#     response = requests.get(url=url, headers=headers).content.decode('utf-8')
#     with open('知乎第{}页.html'.format(page+1), 'w', encoding='utf-8')as f:
#         f.write(response)
#
#     print(response)

# 补充内容:1.requests.request
# requests.request(method='get', url=full_url)

#get请求参数:
parems = {"kw": "python", "fr": "search", "red_tag": "t3476000044"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
url = 'http://tieba.baidu.com/f?'
response = requests.request('get', url=url, parems=parems, headers=headers).content.decode('utf-8')
print(response)