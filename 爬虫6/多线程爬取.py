import requests, os, re, threading
from lxml import etree
from urllib import request
from queue import Queue


class Procuder(threading.Thread):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
        'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=H9lXZA-GCoRI4dxDKLd0jdIoKEpGbfx0XsPGK5KpGnyqxZUmUuazSbddHF8vcmrH&wd=&eqid=ce90d9d2000037f9000000025de36e6c; __cfduid=da8933f2415f9b032170226292ed31f9f1575186047; UM_distinctid=16ec06cc429a5a-0129dc7c79396-47744716-100200-16ec06cc42a80a; CNZZDATA1256911977=633573852-1575184287-null%7C1575184287; _ga=GA1.2.260402182.1575186384; _gid=GA1.2.2003498981.1575186384; __gads=Test; XSRF-TOKEN=eyJpdiI6IlVHV1pBQkV4K3dcL2Q2NW5UR1BsaGVBPT0iLCJ2YWx1ZSI6ImVOeURSZGZEQjc5bnplVE80c1RkU1dkQzFiMjFrc2RReVwvQnpFdkpORWtDaWtlalJKNWtxSmVrOUg5MW5CZUpCIiwibWFjIjoiMmRiMTg3MjdmZTdkMjFhNDI1MjA3ZDg4OGVkNDUyMWU1OWZlM2JlZjNlNTM3NTY3MWY1NDBhNTNlMmU0ODNjZiJ9; doutula_session=eyJpdiI6IlNmekFlNUROb21jcTdoTEtWRU1SakE9PSIsInZhbHVlIjoiNm42T01Hbk9QTHZhNTJYRkpCKzF4SldSSlg0Mk9sZ2JSdkFSZEZDVEpMU2FCRm1OWWhTSDhYQ3ZTZ1lmZTMyUyIsIm1hYyI6IjgxYmE4MGFjNWYxMDhhNDBkOWEzNDdmMGQwNDdjMzNkYmJmNjgwYjkyNTZlZTk2ZTAxMjA4OGM3NDFlNDdmNzgifQ%3D%3D'
        }
    def __init__(self, page_queus, img_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queus
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url=url, headers=self.headers).text
        html = etree.HTML(response)
        imgs = html.xpath("""//div[@class="page-content"]//img[@class!="jpg"]""")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.，。!！\*]','',alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt+suffix

            self.img_queue.put((img_url, filename))

class Consumer(threading.Thread):
    def __init__(self, page_queus, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.parse_page = page_queus
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.parse_page.empty():
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, '/python文件夹/img/' + filename)
            print(filename + '下载完成')

def main():
    page_queue = Queue(12)
    img_queue = Queue(1000)
    for n in range(1, 12):
        url = f'http://www.doutula.com/zz/list?page={n}'
        page_queue.put(url)

    for x in range(5):
        t = Procuder(page_queue, img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()

if __name__ == '__main__':
    main()


