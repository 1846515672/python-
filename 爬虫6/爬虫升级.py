from selenium import webdriver

#将selenium与浏览器组合
driver = webdriver.PhantomJS(executable_path=r'G:\python文件夹\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#访问网站
url = 'https://www.zhaopin.com/'
driver.get(url=url)

#拍照
# driver.save_screenshot('boss1.jpg')

#找到输入框,模拟输入
driver.find_element_by_id('zp-search__input').send_keys('python')
