import requests, re, json, random, pymysql
from lxml import etree

host = 'localhost'  # 本地主机
user = 'root'  # 用户名
password = ''  # 数据库密码
database = 'qiye'  # 数据库名称
port = 3306  # 端口号
db = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = db.cursor()

headers = {
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
'cookie': 'acw_tc=2760825315749544513396449e9a2b315a7adc91577fe04386d3a59bfefb26; _uab_collina=157495455154982154428578; x-zp-client-id=282da877-ca68-460a-923f-7d134624af07; sts_deviceid=16eb29b5a5459-0af0b397ca0fa8-47744716-1049088-16eb29b5a55462; adfbid2=0; __utma=269921210.71930086.1574993459.1574993459.1574993459.1; __utmz=269921210.1574993459.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1574993460; dywez=95841923.1574993460.1.1.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; dywea=95841923.2833327427782705000.1574993460.1574993460.1575028705.2; urlfrom2=121126445; adfcid2=none; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216eb29b5ad7460-09d086080d707f-47744716-1049088-16eb29b5ad8560%22%2C%22%24device_id%22%3A%2216eb29b5ad7460-09d086080d707f-47744716-1049088-16eb29b5ad8560%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fjobs.zhaopin.com%2FCC508620126J00440894805.htm; jobRiskWarning=true; acw_sc__=5de46f30e92f1983383d47f0632e826e378f2c51; ZL_REPORT_GLOBAL={%22jobs%22:{%22recommandActionidShare%22:%226fd97a2a-100f-425a-8bd3-e782deaeec2c-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_sid=16ec453ea7947a-00b1e8dee73f8b-47744716-1049088-16ec453ea7a416; sts_evtseq=2'
}

for i in range(530, 950):
    url = f'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId={i}&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.84291309&x-zp-page-request-id=7b385f2290c34b158628d457c9106474-1574951994337-724556&x-zp-client-id=73997459-9ada-45e4-8a58-9d7dd5e23234&MmEwMD=4UKWV9k8jEULO9xOncHvEwtgniWZZGWjDY82YV6y9WzljfNb_wEv56r0_X_NoqTEeHzqA3FvFcAlMK8Xl3veTTMex1eLUPAuKiE7b6dOkSdEoCdMGNa8pXrq4_soMr5O7ycZboSqmKOLUKrRMcJCmEG.NbI7RfCu74Qaj3ox800qePkxW7Ob4r0GzSf_5BP30teMix_HBLjmFef6H_vcdp2Yhj9qhEPd7E6FmFw1rLAmrf7tMWP_qXHGF8QVqH8vT7t89EgoCBxTJkn.XujFo6S0Ys2ntXL.J4KMEDbw.jH0iaonyOoAXE8PV6sYOmAmGguJaqyJaLWncosGLrvpnRO2wZ_Jm_HFioW5ofG9lEjMbNyrN7XHpWyKcD4UhX09hVOXCDEB.O8H6nes1o5LPAbct'
    print(url)
    response= requests.get(url=url, headers=headers).content.decode('utf-8')
    response = json.loads(response)
    if response is None:
        continue
    else:
        # print(response)
        firm_list1 = []
        firm_list = []
        for post in response["data"]["results"]:
            # 公司详情页地址
            resp = requests.get(url=post.get("positionURL"), headers=headers).content.decode('utf-8')
            tree_to = etree.HTML(resp)
            # 职位亮点
            Selling_Points = tree_to.xpath('.//div[@class="highlights"]//span[@class="highlights__content-item"]/text()')
            Selling_Points = ",".join(Selling_Points)

            # 岗位要求
            # 任职要求
            job_requirements = tree_to.xpath('//div[@class="describtion__detail-content"]//div/text()')
            strjob = "".join(job_requirements).replace(' ', '')

            # 技能要求；
            Skill = tree_to.xpath('//div[@class="describtion__skills"]//div/span/text()')
            Skill = ",".join(Skill)
            # 工作地点；
            workplace = tree_to.xpath('//div[@class="job-address clearfix"]/div[@class="job-address__content"]/span/text()')
            if workplace is not None:
                workplace = workplace[0]
            else:
                continue
            # 薪资水平，
            wage_level = tree_to.xpath('//div[@class ="summary-plane__bottom"]/div/span/text()')
            if wage_level is not None:
                wage_level = wage_level[0]
            else:
                continue
            boos_dict1 = {'职位名称':post.get("jobName"), '公司名称':post.get("company").get("name"),
                          '公司规模':post.get("company").get("size").get("name"), '公司类型':post.get("company").get("type").get("name"),
                          '公司详情页地址':post.get("positionURL"), '职位亮点':Selling_Points, '岗位要求':strjob,
                          '技能要求':Skill, '工作地点':workplace, '薪资水平':wage_level}
            print(boos_dict1)

            # 岗位发布网站（如智联招聘）
            # 智联招聘
            sql1 = f"""insert into zhilian(职位名称,公司名称,公司规模,公司类型,公司详情页地址,职位亮点,岗位要求,技能要求,工作地点,薪资水平)
            values("{boos_dict1['职位名称']}","{boos_dict1['公司名称']}","{boos_dict1['公司规模']}",
            "{boos_dict1['公司类型']}","{boos_dict1['公司详情页地址']}","{boos_dict1['职位亮点']}",
            "{boos_dict1['岗位要求']}","{boos_dict1['技能要求']}","{boos_dict1['工作地点']}",
            "{boos_dict1['薪资水平']}")"""
            cursor.execute(sql1)
            db.commit()
