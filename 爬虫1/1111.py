import requests
import json,random

#随机主机
proxies = [
    {
        "http": "175.42.129.149:9999",
        "https": "175.42.129.149:9999"
    },
    {
        "http": "175.42.129.149:9999",
        "https": "175.42.129.149:9999"
    }
]
#随机头
headers = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
    },

]
#通过指定的adcode码获取天气的详细信息,并返回需要打印到txt中的数据
def get_tianqi(dict):
    #拼接
    url = "https://www.amap.com/service/weather?adcode="
    url = url+dict["adcode"]
    response = requests.get(url=url, headers=random.choice(headers)).content.decode("utf-8")
    response = json.loads(response)
    #通过请求回来的json数据逐层筛选
    data_now = response["data"]["data"][0]
    data_tomorow = response["data"]["data"][1]

    return ("{}  当前时间:{},天气:{},温度:{},明天天气:{},最高气温:{},最低气温:{}".format(dict["name"],data_now["report_time"], data_now["live"]["weather_name"],data_now["live"]["temperature"],data_tomorow['report_time'],data_tomorow['forecast_data'][0]['max_temp'],data_tomorow['forecast_data'][0]['min_temp']))

# 获取到所有的城市
def cityes():
    url = "https://www.amap.com/service/cityList?version=201911219"
    response = requests.get(url=url,headers=random.choice(headers)).content.decode("utf-8")
    response = json.loads(response)
    all_cities = []

    for i in response["data"]["cityData"]["provinces"]:
        # print("省份:{}".format(response["data"]["cityData"]["provinces"][i]["name"]))
        province = response["data"]["cityData"]["provinces"][i]["name"]  #省份
        if response["data"]["cityData"]["provinces"][i]["cities"]:
            cities = response["data"]["cityData"]["provinces"][i]["cities"]
            for i in cities:
                all_cities.append({"name":i["name"],"adcode":i["adcode"]})
        else:
            cities = response["data"]["cityData"]["provinces"][i]["label"]
            all_cities.append({"name":response["data"]["cityData"]["provinces"][i]["name"],"adcode":response["data"]["cityData"]["provinces"][i]["adcode"]})
    return all_cities

#保存
def save(responce):
    with open("html/tianqi2.txt","a",encoding="utf-8") as f:
        f.write("{}\n".format(responce))


if __name__ == '__main__':
    cities = cityes()
    for city in cities:
        response = get_tianqi(city)
        save(response)
