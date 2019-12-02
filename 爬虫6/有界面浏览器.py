from selenium import webdriver
from lxml import etree
import time


driver = webdriver.Chrome(executable_path=r'G:\python文件夹\爬虫\chromedriver.exe')
url = 'https://www.taobao.com/'
driver.get(url=url)

#1拍照
driver.save_screenshot('taobao1.png')

#2找到输入框模拟输入
driver.find_element_by_id('q').send_keys('袜子')


#3拍照
driver.save_screenshot('taobao2.png')

#4点击
driver.find_element_by_xpath('//ul[@class="service-bd"]/li[1]/a[2]').click()

#5隐士等待10秒钟,超过10秒网页还没有加载就报错
driver.implicitly_wait(10)

#6拍照
# driver.save_screenshot('taobao4.png')

#7拉动下滑条需要用到的js操作
for x in range(1, 8):
    time.sleep(1.5)
    j = x/10
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f'%j
    driver.execute_script(js)
