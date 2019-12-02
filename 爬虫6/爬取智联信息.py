from lxml import etree
from selenium import webdriver

dirver = webdriver.PhantomJS(executable_path=r'G:\python文件夹\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'https://sou.zhaopin.com/?jl=530&sf=0&st=0&kw=python%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3'
dirver.get(url)

# with open('智联.html', 'w', encoding='utf-8')as f:
#     f.write(dirver.page_source)

tree = etree.HTML(dirver.page_source)
# 岗位名称
job_dict = {}
Job_Title = tree.xpath('//div[@class="contentpile__content__wrapper__item__info__box__jobname jobName"]/span/text()')
job_dict['岗位名称'] = Job_Title
# print(job_dict['岗位名称'])
# 公司名称
company_name = tree.xpath('.//div[@class="contentpile__content__wrapper__item clearfix"]//a[@class="contentpile__content__wrapper__item__info__box__cname__title company_title"]/text()')
# print(company_name)
job_dict['公司名称'] = company_name
# 公司人数或公司规模（例如：500~1000人）

# 公司类型（国企）
# company_type =
# 岗位要求
# 技能要求
# 工作地点
# 薪资水平
# 任职资格
# 岗位发布网站（如智联招聘）