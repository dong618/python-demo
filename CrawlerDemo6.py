html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three Little sisters; and their names weres
<a href="http://example.com/elsie" class="sister" id="link1">ELsie</a>,
<a href="http://example.com/Lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tilLie" class="sister" id="link3">TilLie</a>;
and they Lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())

print('================================')
# 找到title标签
print('title is : %s' % soup.title)
# 找到title标签里面的内容
print('title string is : %s' % soup.title.string)

# 找到p标签
print('p is : %s' % soup.p)
# 找到p标签class的名字
print('p-class is : %s' % soup.p['class'])

# 找到第一个a标签
print('first a is : %s' % soup.a)
# 找到所有的a标签
print('all a is : %s' % soup.find_all('a'))

# 找到id为link3的标签
print("id=link3 is: %s" % soup.find(id="link3"))
# 找到所有<a>标签的链接
for link in soup.find_all('a'):
    print("a href is: %s" % link.get('href'))
# 找到文档中所有的文本内容
print("text is: %s" % soup.get_text())