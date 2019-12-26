'''
    Day 2 视频观看：
    4）requests库的基本使用
    5）结合正则表达式爬取图片链接

    💯Day 2 作业：
    使用 requests 库配合正则表达式，获取豆瓣读书 book.douban.com/top250 排名最高的25本书的名字。

    参考资料：
    re：https://docs.python.org/zh-cn/3/library/re.html
    requests ：https://2.python-requests.org//zh_CN/latest/user/quickstart.html

    源码参考：
    https://github.com/wilsonyin123/geekbangpython/tree/master/timegeekbang.com

    提交方式：请将自己的「代码+最终排名」截图发送到群内，写明【Day 2 作业打卡】
'''

import requests
import re

url = 'https://book.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}
response = requests.get(url=url, headers=headers)
print(response.status_code)
if response.status_code == 200:
    content = response.text
    pattern = re.compile(r'<div class="pl2">.*?<a.*?>(.*?)</a>.*?</div>', re.S)
    results = re.findall(pattern, content)
    index = 0
    for result in results:
        index += 1;
        name = re.sub('\s', '', result)
        name = name.replace('<spanstyle="font-size:12px;">', '')
        name = name.replace('</span>', '')
        print('TOP %d <<%s>> ' % (index, name))