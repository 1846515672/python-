import requests
import json

def fanyi(kw):
    # 1.url

    url ='https://fanyi.baidu.com/sug'
    #请求方式;post:

    #2.参数：
    data = {'kw': kw}

    #3.请求：
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    response = requests.post(url=url,headers=headers,data=data ).content.decode('utf-8')
    # print(type(response))

    # with open('fanyi.html', 'w', encoding='utf-8')as fp:
    #     fp.write(response)

    #返回页面格式：json: (1)转成python 类型：
    response = json.loads(response)
    print(response)
    for i in response['data']:
        pass
        # print(i)
        # word = i['k']
        # translate = i['v']
        # print(word,':', translate)
#         with open('fanyi.txt', 'a', encoding='utf-8')as fp:
#             fp.write(word+':'+ translate+'\n')
#
if __name__ == '__main__':
#     while True:
        kw = input('请输入翻译的单词')
        fanyi(kw)

