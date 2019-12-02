import requests

# url = 'http://www.renren.com/PLogin.do'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
           'Cookie': 'anonymid=k39tosfn-bmwvod; depovince=BJ; _r01_=1; _de=44AF7B01DBD520AA47FF32E183E77DAB; __utma=151146938.1588740241.1574408227.1574408227.1574408227.1; __utmz=151146938.1574408227.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ln_uact=15282771516; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=2fce98b7-3918-4a9b-8aee-eff55c1df116%7Cd62998c0d42f00cd3a83c9111d9fe295%7C1574408202710%7C1%7C1574408303290; wp=0; wp_fold=0; jebe_key=2fce98b7-3918-4a9b-8aee-eff55c1df116%7Cd62998c0d42f00cd3a83c9111d9fe295%7C1574408202710%7C1%7C1574650246346; jebecookies=50e300a4-43fd-417f-bd68-faf93c3ffa9e|||||; JSESSIONID=abcxsNc36Zy_Hfb7SDG6w; ick_login=d64fdf2e-09e4-486b-ae8d-5106c3f87d15'}
# data = {"email":'15282771516', 'password':'xujin1846515672'}
#
# response = requests.post(url=url, data=data, headers=headers).content.decode('utf-8')
# with open('renrenwang.html', 'w', encoding='utf-8')as fp:
#     fp.write(response)

#创建session对象
sess = requests.session()

#模拟登陆,记录客户端身份信息
url = 'http://www.renren.com/PLogin.do'
data = {"email":'15282771516', 'password':'xujin1846515672'}
sess.post(url=url, data=data)
#访问首页信息
response = sess.get("http://www.renren.com/380463436/newsfeed/photo").content.decode('utf-8')
with open('人人网首页.html', "w", encoding='utf-8') as f:
    f.write(response)
print(response)