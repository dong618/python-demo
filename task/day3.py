'''
    ‍Day 3 视频观看：
    6）Beautiful Soup的安装和使用

    💯Day 3 作业：
    1. 使用 Beautiful Soup 筛选器代替正则表达式进行图书名字筛选。
    2. 通过搜索引擎了解 Xpath 的功能并比较和 Beautiful Soup 的差异。

    参考资料：
    Beautiful Soup：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
    XPath：https://developer.mozilla.org/zh-CN/docs/Web/XPath

    源码参考：
    https://github.com/wilsonyin123/geekbangpython/tree/master/timegeekbang.com

'''

from bs4 import BeautifulSoup
import requests

url = 'https://book.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}
response = requests.get(url=url, headers=headers)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())
    index = 0
    for title_href in soup.find_all('div', class_='pl2'):
        for title in title_href.find_all('a'):
            titleName = title.get('title')
            if titleName:
                index += 1
                if title.find_all('span'):
                    for name in title.find_all('span'):
                        print('TOP %d <<%s%s>> ' % (index, titleName, name.string))
                else:
                    print('TOP %d <<%s>> ' % (index, titleName))
