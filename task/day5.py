'''
    Day 5 视频观看：
    8）使用爬虫爬取图片链接并下载图片

    💯Day 5 作业：
    学习异常处理对网络超时、文件不存在等异常进行捕获并处理。

    参考资料：
    错误和异常：https://docs.python.org/zh-cn/3/tutorial/errors.html

'''

from bs4 import BeautifulSoup
import requests
import os
import shutil

url = 'https://book.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}

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
    for pic_href in soup.find_all('a', class_='nbg'):
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')
            if imgurl is not None:
                dir = os.path.abspath('../img/')
                filename = os.path.basename(imgurl)
                imgpath = os.path.join(dir, filename)
                print('开始下载: imgurl is %s, imgpath is %s' % (imgurl, imgpath))
                download_jpg(imgurl, imgpath)
craw3(url)