import requests



url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=3d&issueCount=30'

data={"name": "ssq","issueCount": 100}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

response = requests.get(url=url,headers=headers,data=data).content.decode('utf-8')
print(response)

# with open('renrenwang.html', 'w', encoding='utf-8')as fp:
# #     fp.write(response)