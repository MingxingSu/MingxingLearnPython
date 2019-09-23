import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import html.parser
from MyHtmlParser import MyHtmlParser

url = 'http://www.esdict.cn/home/dailysentence'

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"}

response = urllib.request.urlopen(url, timeout=10)
html = response.read().decode('utf-8')

htmlParser = MyHtmlParser()
htmlParser.feed(html)

data = htmlParser.HTMLData

htmlParser.clean()

for line in data:
    if line[:4] == '每日一句':
        print(line)





