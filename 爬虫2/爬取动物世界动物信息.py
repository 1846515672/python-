import re, requests, json, random

url = 'http://www.iltaw.com/animal/all'
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'__cfduid=d3ede3a7215425e5a46a017d018ff21181574672798; PHPSESSID=2e467e45d7ce6820cf34573b32e7c8a0; Hm_lvt_2b65b835db5cae63ad487fd29631b1c7=1574672902; Hm_lpvt_2b65b835db5cae63ad487fd29631b1c7=1574672902; UM_distinctid=16ea1d1a881a7-03bf7bf3ddb6a3-47744e16-100200-16ea1d1a882796; CNZZDATA1000267376=1780083339-1574669922-%7C1574669922',
'Host':'www.iltaw.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
}

proxies = [
{'https': '182.34.34.45:9999'},  # 一般/良好/优秀
{'https': '171.35.147.78:9999'},  # 优秀
{'https': '27.152.25.246:9999'},  # 一般/良好/优秀
{'https': '125.124.19.124:9999'},
{'https': '112.111.77.247:9999'},  # 重残
{'https': '182.35.87.171:9999'},  # 一般/良好
{'https': '171.35.172.192:9999'},  # 良好/优秀
{'https': '117.69.200.134:9999'},  # 优秀
{'https': '183.146.156.71:9999'},  # 良好/优秀
{'https': '117.28.96.160:9999'},  # 良好/优秀
{'http': '119.123.177.155:9000'},  # 正常
{'https': '124.16.81.135:1080'},  # 正常
{'http': '123.117.34.115:9000'},  # 正常
{'https': '180.103.218.209:8118'},  # 正常
{'http': '163.125.65.166:9797'},  # 正常
{'https': '118.31.9.50:8118'},  # 正常
{'http': '49.70.89.81:9999'},  # 正常
{'https': '182.88.5.99:9797'},  # 正常
{'http': '27.152.91.208:9999'},  # 正常
{'https': '49.70.48.74:9999'},  # 正常
{'http': '27.43.187.82:9999'},  # 正常
{'https': '117.57.91.201:9999'},  # 正常
{'http': '27.43.184.101:9999'},  # 正常
{'https': '114.239.3.40:808'},  # 正常
{'http': '182.35.80.184:9999'},  # 正常
{'https': '182.35.83.219:9999'},  # 正常
{'http': '113.124.94.55:9999'},  # 正常
{'https': '113.124.95.237:9999'},  # 正常
]

proxies = random.choice(proxies)

response = requests.get(url=url, headers=headers).content.decode('utf-8')
print(response)
