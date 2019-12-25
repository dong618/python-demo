from bs4 import BeautifulSoup
import requests

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

url = 'https://xclient.info/a/'

#取得标题
def craw2(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for title_href in soup.find_all('div', class_='archive-main'):
        print([title.get('title')
               for title in title_href.find_all('a') if title.get('title')])

# 运行结果
# ['经验分享', '软件教程', '新闻资讯', '正版软件优惠活动介绍', '官方正版绑定账户 AdGuard 广告拦截隐私保护软件 3设备授权', 'iSlide for Mac版正式发布', 'ZMI紫米65W桌面三口充电器 限时特惠']
# craw2(url)


for i in range(1, 5, 1):
    url = 'https://xclient.info/a/' + str(i)
    # print(url)
    craw2(url)