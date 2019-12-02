import requests,json

url = "https://www.amap.com/service/cityList?version=2019103020"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

response = requests.get(url=url,headers=headers).content.decode("utf-8")
response=json.loads(response)


for cities in response["data"]["cityByLetter"]:
    for city in response["data"]["cityByLetter"][cities]:
        whether_url = "https://www.amap.com/service/weather?adcode="

        try:
            full_url = whether_url + city["adcode"]
            response=requests.get(url=full_url,headers=headers).content.decode("utf-8")
            print("{}:{}".format(city["name"],response))

        except Exception as e:
            continue
