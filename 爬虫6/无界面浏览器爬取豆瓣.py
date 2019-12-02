from selenium import webdriver
from lxml import etree

url = 'https://book.douban.com/'
driver = webdriver.PhantomJS(executable_path=r'G:\python文件夹\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get(url=url)

#模拟快照
# driver.save_screenshot('豆瓣读书.jpg')
# with open('豆瓣读书.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_source)

#提取信息
tree = etree.HTML(driver.page_source)
douban = tree.xpath('.//div[@class="carousel"]/div[@class="slide-list"]/ul[2]/li/div[@class="cover"]/a/@title')
# print(douban)