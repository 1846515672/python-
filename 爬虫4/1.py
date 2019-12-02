from lxml import etree
import requests, random


# 定义链家信息列表
lianjia_info_list = []
for i in range(1, 2):
    url = f'https://bj.fang.lianjia.com/loupan/pg{i}/'

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'Cookie':'lianjia_ssid=a80e7c16-b4c5-41cf-96a8-41b6561752bb; lianjia_uuid=f325a111-1b89-4368-9fe7-d528a29a0c96; UM_distinctid=16eac8e077f481-0b354303b8bc7c-47744716-100200-16eac8e078038d; CNZZDATA1256144455=1819133882-1574851404-%7C1574851404; CNZZDATA1254525948=1389752876-1574851908-%7C1574851908; CNZZDATA1255633284=917502763-1574851968-%7C1574851968; CNZZDATA1255604082=324589487-1574851813-%7C1574851813; _ga=GA1.2.1303853658.1574853020; _gid=GA1.2.797308973.1574853020; _jzqa=1.1720901128070906600.1574853020.1574853020.1574853020.1; _jzqc=1; _jzqckmp=1; _qzjc=1; gr_user_id=fe2fc801-cd77-4d62-b54a-d5edfdb4e6f6; gr_session_id_a1a50f141657a94e=c7895dd7-88e7-40f4-91e5-4088ae679870; gr_session_id_a1a50f141657a94e_c7895dd7-88e7-40f4-91e5-4088ae679870=true; select_nation=1; ljisid=f325a111-1b89-4368-9fe7-d528a29a0c96; _smt_uid=5dde59d1.15dbf491; _jzqa=1.307533322688845900.1574853074.1574853074.1574853074.1; _jzqc=1; _jzqx=1.1574853074.1574853074.1.jzqsr=i%2Elianjia%2Ecom|jzqct=/us.-; _jzqckmp=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216eac8edeb43cd-0d5869f2d20474-47744716-1049088-16eac8edeb548d%22%2C%22%24device_id%22%3A%2216eac8edeb43cd-0d5869f2d20474-47744716-1049088-16eac8edeb548d%22%2C%22props%22%3A%7B%7D%7D; select_city=110000; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _jzqb=1.2.10.1574853074.1; _gat_past=1; search_position=default_list; _qzja=1.910622990.1574853019998.1574853019998.1574853019999.1574853152935.1574853158637.0.0.0.10.1; _qzjb=1.1574853019998.10.0.0.0; _qzjto=10.1.0; _jzqb=1.3.10.1574853074.1; srcid=eyJ0IjoiXCJ7XFxcImRhdGFcXFwiOlxcXCJkMjc5ZWNkZmIxMTcxMGViYWUyYWYzYmE4ODVlODgwZDZkM2E2NjEzNWY3ODM1YzU0YzM4ZGFkZGFmODY4OTBlZjc4MjBlZGZmNGI3YjRiZjNjOGVhY2JmZGE1Y2M5ZDgxZmMxMDgzNTA5ZDM3ZGQ5NjE0MGVlYTI1NmJkMzIwM2VhZWM3MDMxMWVlMDZkZDBmNzQzNDY2OGRmMGVmZGRkMmU2MjJjZjE2MWFlNjc5NzkwNzVmODgwMDIwNzRmY2UzMzI3M2FhMjg5YTRjM2QwOGMzZjY3MDM4M2QzZmRmMDNhOTAwYzg2YTZhY2M5ZmQzMWJiNTA4NjNhZDk1ZjMwMWRlNGU4YmU4NWZjZWZiZGFiOTQzMGVmN2YzYTVhYTVmNWE4MTIxMGJhMDMyYzBhYTMzNzM3Y2RmMzQxYTNiNTZmMTMxMjIzN2E3ZWRjZmRmZTExNjY1MGFhYzhmYzc2XFxcIixcXFwia2V5X2lkXFxcIjpcXFwiMVxcXCIsXFxcInNpZ25cXFwiOlxcXCIwZjc1MGI3OVxcXCJ9XCIiLCJyIjoiaHR0cHM6Ly9iai5mYW5nLmxpYW5qaWEuY29tL2xvdXBhbi8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; lj_newh_session=eyJpdiI6Ik5IZ0NJN3RPRWorSEFNVjNVdThiNlE9PSIsInZhbHVlIjoiWVNDZ2R3MG9YOWZnZ0JOem9FXC96MVFBOUVVSDBEYm9BK1N2RExLUEdVVm5XZUpOU0lJbk1ERTFPY3NXb2RzRzd5R1ZNQ2pOYnRSV1BlOXpNK3YyOWVBPT0iLCJtYWMiOiJmNTdjZmQ5ZWY0YzQxZTg1OWUxOTdlMTA1NjdiNTc2YzdmMjA3ZThhNTEwZjEzOTk3NGVmYmI1YjY1ZDNiMGE1In0%3D',
    }
    proxies = [
        {'http': '183.154.50.164:9999'},# 正常
        {'http': '182.35.81.65:9999'},# 正常
        {'http': '114.239.255.34:9999'},# 正常
    ]
    proxies = random.choice(proxies)

    response = requests.get(url=url, headers=headers, proxies=proxies).content.decode('utf-8')
    # 定义链家信息字典
    lianjian_info_dict = {}
    lianjia = etree.HTML(response)
    site = lianjia.xpath('.//div[@class="resblock-location"]/a/text()')
    print(site)
    for dizhi in site:
        lianjian_info_dict['链家地址'] = dizhi

