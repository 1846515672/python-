from selenium import webdriver
import time, re



def search_product():
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(k)
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    driver.implicitly_wait(100)#隐士等待，等待验证所停留的时间,可以给长一点，避免浏览器网速卡顿或者网络不畅通情况下加载不完全。
    token = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('(\d+)').search(token).group(1))
    return token

def drop_down():
    # 缓慢拉动拉动下滑条
    for x in range(1, 10):
        time.sleep(1.5)
        j = x / 10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

def get_product():
    # 获取所有的div,然后遍历所有的div,得到一个div,再去div里面寻找我们要找的数据,任意位置
    divs = driver.find_element_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        image = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        price = div.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price')+'元'
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        name = div.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        product = {'标题':info, '价格':price, '订单量':deal, '图片':image, '名称':name}
        print(product)


def net_page():
    token = search_product()
    drop_down()
    get_product()
    num = 1
    while num != token:
        driver.get(f'https://s.taobao.com/search?q={k}&s={44*num}')
        #无限循环可能造成卡顿
        driver.implicitly_wait(100)#隐士等待,最高等待时间100秒,超过100秒抛出异常
        num += 1
        drop_down()
        get_product()


if __name__ == '__main__':
    k = input('请输入你需要查询的商品:')
    driver = webdriver.Chrome(r'G:\python文件夹\爬虫\chromedriver.exe')
    driver.get('https://www.taobao.com/')
    net_page()
