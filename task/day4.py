'''
Day 4 视频观看：
7）使用爬虫爬取新闻网站

💯Day 4 作业：
使用 requests 和 XPath 获取豆瓣 top250 图书名字和作者，保存至本地文件。

参考资料：
Python I/O：https://docs.python.org/zh-cn/3/library/io.html

'''

from bs4 import BeautifulSoup
import requests, os

url = 'https://book.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}
response = requests.get(url=url, headers=headers)
# print(response.status_code)
myList = []
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
                        str = 'TOP %d <<%s%s>> ' % (index, titleName, name.string)
                        myList.append(str)
                else:
                    str = 'TOP %d <<%s>> ' % (index, titleName)
                    myList.append(str)
    file_write_obj = open("../txt/day4.txt", 'w', encoding='utf-8')
    for txt in myList:
        file_write_obj.writelines(txt)
        file_write_obj.write('\n')