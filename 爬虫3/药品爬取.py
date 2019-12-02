import re, json, requests, random

for i in range(1, 2):
    url = f'https://www.111.com.cn/categories/953710-j{i}.html'
    headers = {
    'cookie':'locateCityName=%E4%B8%8A%E6%B5%B7; locateProvinceName=%E4%B8%8A%E6%B5%B7; locateProvinceId=1; UUID=aCEe7D0a-dBDa-4bE-aAD7-AD9DbBbf6B67; provinceId=1; cartKey=2cb35e864bb8a1438d03f576a9eeb170; demandItemCount=0; Hm_lvt_4674a7b9bc5deca972145cfd7f6cb592=1574774745; locateProvinceId=2; locateProvinceName=%E5%8C%97%E4%BA%AC; locateCityName=%E5%8C%97%E4%BA%AC; cityName=%E5%8C%97%E4%BA%AC; history=51347632%2C%20%E8%89%BE%E8%BF%AA%E8%8E%8E%20%E7%BE%8E%E6%B2%99%E6%8B%89%E7%A7%A6%E7%BC%93%E9%87%8A%E9%A2%97%E7%B2%92%E5%89%82%200.5g*10%E8%A2%8B%2F%E7%9B%92%20%E7%BB%93%E8%82%A0%E7%82%8E%20%E5%85%8B%E7%BD%97%E6%81%A9*20%E4%BB%B6%3B%2050658844%2C%20%E4%B8%87%E8%89%BE%E5%8F%AF%20%E6%9E%B8%E6%A9%BC%E9%85%B8%E8%A5%BF%E5%9C%B0%E9%82%A3%E9%9D%9E%E7%89%87%2050mg*10%E7%89%87*3%E4%BB%B6%3B%2050090796%2C%20%E5%BC%80%E6%B5%A6%E5%85%B0%20%E5%B7%A6%E4%B9%99%E6%8B%89%E8%A5%BF%E5%9D%A6%E7%89%87%200.5g*30%E7%89%87*10%E4%BB%B6%3B%2050689627%2C%20%E9%87%91%E6%88%88%20%E6%9E%B8%E6%A9%BC%E9%85%B8%E8%A5%BF%E5%9C%B0%E9%82%A3%E9%9D%9E%E7%89%87%EF%BC%88%E4%BC%9F%E5%93%A5%EF%BC%89%2050mg*20%E7%89%87*2%E4%BB%B6%3B%20; JSESSIONID=E988AA3F8C751BAA2BF337B0BFFE4EFD; cururl=https%3A%2F%2Fwww.111.com.cn%2Fcategories%2F953710-j50.html; Hm_lpvt_4674a7b9bc5deca972145cfd7f6cb592=1574775432',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    }
    proxies = [
        {'http': '183.154.50.164:9999'},
        {'http': '182.35.81.65:9999'},
        {'http': '114.239.255.34:9999'},
    ]
    proxies = random.choice(proxies)
    response = requests.request(method='get', url=url, headers=headers, proxies=proxies).content.decode('GBK')
    # with open('药品信息.html', 'w', encoding='utf-8')as f:
    #     f.write(response)
    # print(response)
    drug_price_pattern = re.compile(r'<span>(.*?)<u>', re.S)
    drug_list = drug_price_pattern.findall(response)
    # print(drug_price)
    for drug in drug_list:
        with open('商品信息.html', 'w', encoding='utf-8')as f:
            f.write(drug)
        print(drug)
        drug_pattern = re.compile(r'<span>(\d)</span>', re.S)
        drug_price = drug_pattern.findall(drug)
        print(drug_price)