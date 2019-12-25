from bs4 import BeautifulSoup
import requests
import os
import shutil

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1;",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}


url = 'https://xclient.info/'

def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)

#取得图片
def craw3(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())
    for pic_href in soup.find_all('div', class_='index-main row'):
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            if imgurl is not None:
                dir = os.path.abspath('./img/')
                filename = os.path.basename(imgurl)
                imgpath = os.path.join(dir, filename)
                print('开始下载: imgurl is %s, imgpath is %s' % (imgurl, imgpath))
                download_jpg(imgurl, imgpath)



craw3(url)