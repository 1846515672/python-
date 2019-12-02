import requests, json, re

url = 'https://maoyan.com/board'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'}
response = requests.get(url=url, headers=headers).content.decode('utf-8')
with open('猫眼电影.html', 'w', encoding='utf-8')as f:
    f.write(response)
#1.电影块数量
paers = re.compile(r'<dd>[\d\D]*?</dd>')
dd_list = paers.findall(response)

#2.电影信息
movie_list = []
for move in dd_list:
    movie_dict = {}
    # 电影名字
    title_pattern = re.compile(r'}">(.*?)</a></p>')
    title = title_pattern.findall(move)[0]
    movie_dict['电影名'] = title
    print(movie_dict['电影名'])
    movie_dict['电影名'] = title
    #排名
    rink_pattern = re.compile(r'board-index-(\d+)">')
    rink = rink_pattern.findall(move)[0]
    print(rink)
    movie_dict['电影排名'] = rink
    # 评分
    score_pattern = re.compile(r'<p class="score"><i class="integer">(\d\.)</i><i class="fraction">(\d)</i></p> ')
    score_list = score_pattern.findall(move)
    score = score_list[0][0]+score_list[0][1]
    print(score)
    movie_dict['电影评分'] = score
    #电影链接
    src_pattern = re.compile(r'data-src="(.*?)"')
    src = src_pattern.findall(move)[0]
    print(src)
    movie_dict['电影链接'] = src
    movie_list.append(movie_dict)

# 保存为json文件
data = json.dumps(movie_list, ensure_ascii=False)
with open('猫眼.json', "w", encoding='utf-8') as f:
    f.write(data)