import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
# print(content)

# 网页html代码
# <div class="grid-item work-thumbnail">
#     <a href="http://www.cnu.cc/works/379991" class="thumbnail" target="_blank">
#         <div class="title">恰淡与虚无</div>
#         <div class="author">陈霖享</div>
#         <img src="http://img.cnu.cc/uploads/images/flow/1911/26/1b948553b8df355a93152cad82c12b54.jpg?width=3000&amp;height=2000" alt="恰淡与虚无">
#     </a>
# </div>

# 正则替换
# <div class="grid-item work-thumbnail">
#     <a href="(.*?)" .*?title">(.*?)</div>
#         <div class="author">陈霖享</div>
#         <img src="http://img.cnu.cc/uploads/images/flow/1911/26/1b948553b8df355a93152cad82c12b54.jpg?width=3000&amp;height=2000" alt="恰淡与虚无">
#     </a>
# </div>

pattern = re.compile(r'<a href="(.*?)" .*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
# print(results)

# 解析results
# re.sub('\s', '', name)  \s：匹配空白的字符（可以匹配\n \t 空格等）
for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))