import requests
import random

url = "https://query.aliyun.com/rest/content-platform.api.deliveryInfo?id=8153034&count=10&env=com&cna=uKzqFQr3hgMCAXt05JAurwYu&manual=true&lang=zh"
proxies = [{"http": "223.245.43.38:65309", "https": "14.20.235.95:9797"},
           {"https": "115.200.253.100:8118", "http": "122.224.65.198:3128"},
           {"https": "183.154.54.120:9999", "http": "180.175.16.50:9797"},
           {"https": "115.200.253.100:8118", "http": "125.78.177.186:9999"},
           {"https": "222.89.32.141:8070", "http": "114.239.144.73:808"},
           {"https": "115.200.253.100:8118", "http": "122.224.65.198:3128"}
           ]
prox = random.choice(proxies)
print(prox)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

response = requests.get(url=url, proxies=prox, headers=headers).content.decode('utf-8')
print(response)
