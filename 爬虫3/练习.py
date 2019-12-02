import re, json, requests, random, pymysql

url = 'http://s.askci.com/StockInfo/StockList/GetList'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '159',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'UM_distinctid=16ea781a9f2738-036147f44a0d8a-47744716-100200-16ea781a9f3251; CNZZDATA1261132640=211884611-1574765275-%7C1574765275; Hm_lvt_cee1d5f6521667c816667ee16fb349ab=1574768323; Hm_lpvt_cee1d5f6521667c816667ee16fb349ab=1574768389; RecordRequestProcessingTime=,Application_BeginRequestå¼å§æ¶é´2019-11-26 193903,Application_AuthenticateRequestå¼å§æ¶é´2019-11-26 193903,Application_AuthorizeRequestå¼å§æ¶é´2019-11-26 193903,Application_ResolveRequestCacheå¼å§æ¶é´2019-11-26 193903,Application_AcquireRequestStateå¼å§æ¶é´2019-11-26 193903,Application_PreRequestHandlerExecuteå¼å§æ¶é´2019-11-26 193903,Application_PostRequestHandlerExecuteå¼å§æ¶é´2019-11-26 193903,Application_ReleaseRequestStateå¼å§æ¶é´2019-11-26 193903,Application_UpdateRequestCacheå¼å§æ¶é´2019-11-26 193903,Application_EndRequestå¼å§æ¶é´2019-11-26 193903,Application_PreSendRequestHeaderså¼å§æ¶é´2019-11-26 193903,Application_PreSendRequestContentå¼å§æ¶é´2019-11-26 193903',
    'Host': 's.askci.com',
    'Origin': 'http://s.askci.com',
    'Pragma': 'no-cache',
    'Referer': 'http://s.askci.com/stock/1/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'X-Requested-With': 'XMLHttpRequest',
}
proxies = [
    {'https': '182.34.34.45:9999'},  # 一般/良好/优秀
    {'https': '171.35.147.78:9999'},  # 优秀
    {'https': '27.152.25.246:9999'},  # 一般/良好/优秀
    {'https': '125.124.19.124:9999'},  # 正常"
    {'https': '112.111.77.247:9999'},  # 正常
    {'https': '182.35.87.171:9999'},  # 一般/良好
    {'https': '171.35.172.192:9999'},  # 良好/优秀
    {'https': '117.69.200.134:9999'},  # 优秀
    {'https': '183.146.156.71:9999'},  # 良好/优秀
    {'https': '117.28.96.160:9999'},  # 良好/优秀
    {'https': '124.16.81.135:1080'},  # 正常
    {'https': '180.103.218.209:8118'},  # 正常
    {'https': '118.31.9.50:8118'},  # 正常
    {'https': '182.88.5.99:9797'},  # 正常
    {'https': '49.70.48.74:9999'},  # 正常
    {'https': '117.57.91.201:9999'},  # 正常
    {'https': '114.239.3.40:808'},  # 正常
    {'https': '182.35.83.219:9999'},  # 正常
    {'https': '113.124.95.237:9999'},  # 正常
]
proxies = random.choice(proxies)
firm_list = []
for i in range(1, 2):#572
    data = {'pageNum': i}
    response_to = requests.post(url=url, headers=headers, proxies=proxies, data=data).content.decode('utf-8')
    response = json.loads(response_to)
    for firms in response['data']:
        #公司详情
        firm_dict = {}
        # 2、创建连接
        host = 'localhost'
        user = 'root'
        password = ''
        database = 'qiye'
        # port = 3306
        db = pymysql.connect(host, user, password, database)
        # 3、创建游标对象  监测sql语句执行位置
        cursor = db.cursor()
        #序号
        firm_dict['序号'] = firms["SerialNumber"]
        # 股票代码
        firm_dict['股票代码'] = firms["StockCode"]
        # 股票名称
        firm_dict['股票名称'] = firms["StockName"]
        # 公司全称
        firm_dict['公司全称'] = firms["CompanyName"]
        # 上市日期
        firm_dict['上市日期'] = firms["StrCompanyListingDate"]
        # 公司财报
        firm_dict['公司财报'] = firms["FinancialReport"]
        # 主营业务
        firm_dict['主营业务'] = firms["ProductType"]
        # 行业分类
        firm_dict['行业分类'] = firms["IndustryCategory"]
        # 联系方式
        firm_dict['联系方式'] = firms["phone"]
        # 法人
        firm_dict['法人'] = firms["legalRepre"]
        # firm_list.append(firm_dict)
        # 插入数据
        sql2 = f"""insert into info(序号,股票代码,股票名称,公司全称,上市日期,公司财报,主营业务,行业分类,联系方式,法人) 
        values("{firm_dict['序号']}","{firm_dict['股票代码']}",
       "{firm_dict['股票名称']}","{firm_dict['公司全称']}","{firm_dict['上市日期']}","{firm_dict['公司财报']}",
       "{firm_dict['主营业务']}","{firm_dict['行业分类']}","{firm_dict['联系方式']}","{firm_dict['法人']}")
        """
        # 5、执行sql语句
        cursor.execute(sql2)
        sql = 'show databases'
        cursor.execute(sql)
        # 7、关闭连接
        cursor.close()
        db.close()
# print(firm_list)

