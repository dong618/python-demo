'''
Day 1 作业：
    比较 urllib 和 requests 库的用法差异，通过 random() 方法实现每次提交请求时增加随机的 user-agent HTTP 头部信息。

    参考资料：
    urllib：https://docs.python.org/zh-cn/3/library/urllib.html
    random()：https://docs.python.org/zh-cn/3/library/random.html

    提交方式：请将自己的「代码」截图发送到群内，写明【Day 1 作业打卡】
    https://blog.csdn.net/SEGeeK/article/details/82219829
'''

# urllib
from urllib import request, parse
import random
# requests
import requests

url = 'http://httpbin.org/get'
chromeHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1;",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

sougouHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
}

firefoxHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}
# 采用random 获取headers
headers = random.choice([chromeHeader, sougouHeader, firefoxHeader])

# urlib request.urlopen
req = request.Request(url=url, headers=headers)
response = request.urlopen(req)
print('urllib request.Request: %s \n' % response.read().decode('utf-8'))

# requests requests.get
content = requests.get(url=url, headers=headers).text
print('requests.get: %s \n' % content)
