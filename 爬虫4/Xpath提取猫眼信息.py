from lxml import etree
import requests, random
import pymysql

host = 'localhost'#本地主机
user = 'root'#用户名
password = ''#数据库密码
database = 'maoyan'#数据库名称
port =3306 #端口号
db = pymysql.connect(host=host,user=user,password=password,database=database)
cursor = db.cursor()


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'Cookie': '__mta=255105591.1574837278899.1574837330539.1574837355416.7; uuid_n_v=v1; uuid=9D6E9EE010E111EAACB1A96ED7E7765B8755C565409D44A8A0AA97878E532A1C; _csrf=202ba0b2d65532025ef7be550a2453017b87c6b9e6b351a39613fa7c9c91d393; _lxsdk_cuid=16eab9dd781c8-0eb6dc3fe5041b-5a13331d-100200-16eab9dd782c8; _lxsdk=9D6E9EE010E111EAACB1A96ED7E7765B8755C565409D44A8A0AA97878E532A1C; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1574837279,1574837497; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1574837541; __mta=255105591.1574837278899.1574837532199.1574837540820.9; _lxsdk_s=16eab9dd783-443-c3b-963%7C%7C173'
}
url = 'https://maoyan.com/board'
proxies = [
    {'http': '183.154.50.164:9999'},# 正常
    {'http': '182.35.81.65:9999'},# 正常
    {'http': '114.239.255.34:9999'},# 正常
]
proxies = random.choice(proxies)
response = requests.request(method='get', url=url, headers=headers, proxies=proxies).content.decode('utf-8')
# with open('猫眼电影.html', 'w', encoding='utf-8')as f:
#     f.write(response)
maoyan = etree.HTML(response)
movie_list = maoyan.xpath('//dl[@class="board-wrapper"]/dd')
# print(movie_list)
movie_lists = []
for movie in movie_list:
    movie_dict = {}
    #排名
    ranking = movie.xpath('./i/text()')[0]
    # print(ranking)
    movie_dict['排名'] = ranking

    #名称
    name = movie.xpath('.//p[@class="name"]//a/@title')[0]
    # print(name)
    movie_dict['名称'] = name
    #主演
    star = movie.xpath('.//p[@class="star"]/text()')[0].strip()
    # print(star)
    movie_dict['主演'] = star
    # 上映时间
    time = movie.xpath('.//p[@class="releasetime"]/text()')[0]
    # print(time)
    movie_dict['上映时间'] = time
    # 评分
    grade = movie.xpath('.//p[@class="score"]/i[@class="integer"]/text()')[0]
    grade_to = movie.xpath('.//p[@class="score"]/i[@class="fraction"]/text()')[0]
    # print(grade+grade_to)
    movie_dict['评分'] = grade+grade_to
    sql1 = f"""insert into movie(排名,名称,主演,上映时间,评分)
    values("{ranking}","{name}","{star}","{time}","{grade+grade_to}")"""
    cursor.execute(sql1)
    # sql5 = 'delete from movie'
    # cursor.execute(sql5)
    db.commit()
    movie_lists.append(movie_dict)
print(movie_lists)

cursor.close()
db.close()





