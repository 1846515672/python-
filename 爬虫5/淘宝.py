import requests, re, json, random

list_url = ['https://tce.taobao.com/api/mget.htm?callback=jsonp765&tce_sid=1869682,1869684,1869733,1869809,1869810,1869811,1869812,1869813,1869814,1869816,1869817,1869818,1870204,1870256,1870299,1870321,1871654&tce_vid=3,3,3,1,1,1,1,1,1,1,1,1,1,0,1,2,2&tid=,,,,,,,,,,,,,,,,&tab=,,,,,,,,,,,,,,,,&topic=,,,,,,,,,,,,,,,,&count=,,,,,,,,,,,,,,,,&env=online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online',
            'https://tce.taobao.com/api/mget.htm?callback=jsonp1734&tce_sid=1870303,1870311,1870316,1871653&tce_vid=0,0,2,2&tid=,,,&tab=,,,&topic=,,,&count=,,,&env=online,online,online,online',
            'https://tce.taobao.com/api/mget.htm?callback=jsonp1994&tce_sid=1870341,1870342,1870343,1871657,1871658,1871659&tce_vid=2,2,2,2,2,2&tid=,,,,,&tab=,,,,,&topic=,,,,,&count=,,,,,&env=online,online,online,online,online,online',
            'https://tce.taobao.com/api/mget.htm?callback=jsonp835&tce_sid=1869682,1869684,1869733,1869809,1869810,1869811,1869812,1869813,1869814,1869816,1869817,1869818,1870204,1870256,1870299,1870321,1870333,1870340,1871654,1871655&tce_vid=3,3,3,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,2,2&tid=,,,,,,,,,,,,,,,,,,,&tab=,,,,,,,,,,,,,,,,,,,&topic=,,,,,,,,,,,,,,,,,,,&count=,,,,,,,,,,,,,,,,,,,&env=online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online,online',
]
headers = {
'cookie':'thw=cn; cna=uKzqFQr3hgMCAXt05JAurwYu; t=6447b62179ed13b85dd5d4ea6aa3341f; miid=1551765547307048597; v=0; cookie2=1febaefe22d24c04fccd39f518f9d027; _tb_token_=30e6e333183a3; l=dBNc_11RqcChxIJkBOCiVZ_bSOQOSIRYjuWfhjNBi_5wT6L6MO_OkpXn_Fp6VjWfTn8B4frnxje9-etkiTZNAp46BaKvDxDc.; isg=BD09yid5PIOrOZhL7xUibwZgTJk90BQFDGvZ7_-CeRTDNl1oxyqB_Avk4CrVjYnk',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
}
proxies = [
            {'http': '183.154.50.164:9999'},# 正常
            {'http': '182.35.81.65:9999'},# 正常
            {'http': '114.239.255.34:9999'},# 正常
            {'http': '183.154.50.164:9999'},
            {'http': '182.35.81.65:9999'},
            {'http': '114.239.255.34:9999'},
            {'http': '110.243.27.31:9999'},
            {'http': '27.158.124.217:9999'},
            {'http': '59.57.148.104:9999'},
            {'http': '117.95.214.95:9999'},
            {'http': '182.35.83.189:9999'},
            {'https': '114.230.24.40:9999'},
            {'http': '114.239.198.32:9999'},
            {'http': '117.57.90.130:9999'},
            {'http': '27.152.8.186:9999'},
            {'https': '222.89.32.178:9999'},
            {'https': '114.239.149.118:808'},
            {'http': '113.194.131.125:9999'},
            {'https': '117.69.200.229:9999'},
            {'https': '183.164.239.122:46257'},
            {'http': '117.26.44.97:9999'},
            {'http': '118.212.104.49:9999'},
            {'https': '118.212.106.219:9999'},
            {'http': '59.57.149.2:9999'},
            {'https': '163.204.241.176:9999'},
            {'http': '49.89.87.141:9999'},
            {'https': '114.239.248.77:9999'},
            {'http': '182.35.86.24:9999'},
            {'http': '114.239.29.179:9999'},
            {'https': '49.89.87.72:9999'},
            {'https': '180.122.224.51:9999'},
            {'https': '182.34.33.163:9999'},
            {'https': '27.152.24.224:9999'},
            {'http': '183.164.239.96:9999'},
            {'http': '27.152.91.100:9999'},
            {'http': '114.239.29.16:9999'},
            {'http': '171.35.222.249:9999'},
            {'http': '113.124.95.204:9999'},
            {'http': '49.89.85.83:9999'},
            {'https': '183.154.49.155:9999'},
            {'http': '27.152.8.147:9999'},
            {'https': '114.239.173.198:9999'},
            {'https': '123.54.52.216:9999'},
            {'https': '222.189.190.70:9999'},
            {'http': '183.154.53.102:9999'},
            {'http': '117.57.91.113	40382'},
            {'http': '114.239.254.207:9999'},
            {'http': '114.239.250.10:9999'},
            {'https': '27.152.90.99:9999'},
            {'https': '115.211.231.51:9999'},
            {'http': '117.30.112.105:9999'},
            {'https': '171.35.172.217:9999'},
            {'https': '58.253.157.42:9999'},
            {'http': '58.253.159.126:9999'},
            {'https': '114.239.250.238:9999'},
            {'http': '183.166.20.154:9999'},
            {'http': '117.69.200.197:9999'},
            {'http': '121.226.188.245:9999'},
            {'http': '117.69.51.10:9999'},
            {'http': '114.239.42.205:9999'},
            {'http': '171.35.162.103:9999'},
            {'http': '114.239.1.38:808'},
            {'https': '183.146.157.217:9999'},
            {'https': '120.83.111.153:9999'},
            {'http': '114.239.253.24:9999'},
            {'https': '114.233.49.190:9999'},
            {'http': '183.164.238.97:9999'},
            {'https': '183.166.6.173:9999'},
            {'https': '27.152.90.234:9999'},
            {'http': '182.34.32.230:9999'},
            {'http': '183.164.238.5	21889'},
            {'http': '114.239.254.97:9999'},
            {'http': '114.239.250.196:9999'},
            {'https': '117.69.200.201:9999'},
            {'https': '114.239.1.155	808'},
            {'http': '106.111.53.184:9999'},
            {'https': '114.239.248.199:9999'},
            {'https': '182.35.83.180:9999'},
            {'https': '121.205.84.241:9999'},
            {'https': '171.35.223.208:9999'},
            {'https': '114.239.251.43:9999'},
            {'https': '114.239.252.100:9999'},
            {'https': '120.83.99.122:9999'},
            {'http': '49.70.94.204:9999'},
            {'https': '113.194.48.33:9999'},
            {'http': '182.34.37.196:9999'},
            {'https': '112.87.69.48:9999'},
            {'https': '120.83.107.187:9999'},
            {'http': '106.122.168.237:9999'},
            {'https': '110.243.16.192:9999'},
            {'https': '183.164.238.144:9999'},
            {'http': '114.239.0.57:808'},
            {'http': '171.35.170.4:9999'},
            {'http': '60.13.42.242:9999'},
            {'http': '27.152.8.135:9999'},
            {'http': '120.83.109.73:9999'},
            {'http': '113.195.152.178:9999'},
            {'http': '49.70.89.201:9999'}
]
proxies = random.choice(proxies)
taobao_list = []

for i, url in enumerate(list_url):
    response = requests.get(url=url, headers=headers, proxies=proxies).content.decode('utf-8')
    taobao_pattern = re.compile(r'({.*})', re.S)
    taobao = taobao_pattern.findall(response)[0]
    taobao_data = json.loads(taobao)["result"]
    # print(taobao_data)
    data_pattern = re.compile(r'(tce_sid=[\d,\d]*)')
    list_url_num = data_pattern.findall(url)[0].replace('tce_sid=', "")
    url_num = list_url_num.split(',')

    for info in url_num:
        taobao_too = taobao_data[info]["result"]
        for t in taobao_too:
            taobao_dict = {}
            #产品链接
            product_link = t.get("link")
            taobao_dict['产品链接'] = product_link
            #产品名称
            product_name = t.get("text")
            taobao_dict['产品名称'] = product_name

            taobao_list.append(taobao_dict)
print(taobao_list)