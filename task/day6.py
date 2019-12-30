'''
    �Day 6 作业：
    通过豆瓣 Top250 的 <a> 标签，请求图书详细页，获取前 10 本书的短评，并保存至本地文件。
    参考资料：

    HTML 超链接：https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks

    提交方式：请将自己的「代码+最终排名」截图发送到群内，写明【Day 6 作业打卡】
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