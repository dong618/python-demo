from urllib import request, parse

url = 'http://httpbin.org/post'

'''
    说明: 
     headers中有"Accept-Encoding": "gzip, deflate, sdch", 时，运行报错
     Traceback (most recent call last):
         File "D:/python/python-demo/CrawlerDemo3.py", line 28, in <module>
            print(response.read().decode('utf-8'))
     UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
     
     这个请求无法成功，是因为headers中设置了Accept-Encoding参数，这个参数的存在，相当于告诉服务器，浏览器支持gzip压缩。因此，服务器就会在生成原生response后将其进行gzip压缩，而后把经过压缩的response返回给浏览器，浏览器对其进行解压缩。
     因此，在这个案例中，返回的response其实是经过gzip压缩了的，所以无法直接用utf8进行解码。解决办法：
     删除Accept-Encoding参数，让服务器直接返回未经压缩的response

'''


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1;",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

dict = {
    'name': 'value'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
