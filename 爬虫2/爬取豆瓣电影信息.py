import requests, json
for ii in range(5):
    i = ii * 20
    url = f'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={i}&limit=20'

    headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'ll="108288"; bid=ruLmAQifGoc; __yadk_uid=JVsWNaAmKIJUsRit0uQFS5LicdTk3aUq; _vwo_uuid_v2=D3F25892C38E42C058091C914280BBEBB|6dc22cfee15a629524517a8c27e5b089; douban-fav-remind=1; ap_v=0,6.0; __utma=30149280.57423992.1568212285.1574227413.1574659723.4; __utmc=30149280; __utmz=30149280.1574659723.4.4.utmcsr=video.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.1.10.1574659723; __utma=223695111.242329633.1568212285.1570450115.1574659738.3; __utmb=223695111.0.10.1574659738; __utmc=223695111; __utmz=223695111.1574659738.3.3.utmcsr=sogou.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1574659739%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3D58p16RfDRLsoEW7-fhdQHyttFMzq2zRureaVHN88tHY.%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=5fe96db4d5642442.1568212285.3.1574660221.1570450236.',
    'Host':'movie.douban.com',
    'Pragma':'no-cache',
    'Referer':'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
    'X-Requested-With':'XMLHttpRequest',
    }

    response = requests.get(url = url, headers=headers).content.decode('utf-8')
    response = json.loads(response)
    move_list = []
    for moves in response:
        move_dict = {}
        move_dict['电影名'] = moves.get("title")
        move_dict["电影链接"] = moves.get("url")
        move_dict["评分"] = moves.get("score")
        move_dict["演员"] = moves.get("actors")
        move_list.append(move_dict)

# 写入json
data_json = json.dumps(move_list, ensure_ascii=False)
with open('movie.json', 'w', encoding='utf-8')as f:
    f.write(data_json)
    print(data_json)
    print(type(data_json))
