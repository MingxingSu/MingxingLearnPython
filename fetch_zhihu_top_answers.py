import urllib.request
import urllib.error
from os import remove
from os.path import exists
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from commutils import CommonUtils

htmlBodyTag = r'<html lang="zh"><body>{0}</body></html>'
url = 'https://www.zhihu.com/topic/19776749/top-answers'

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"}

broswer = webdriver.Firefox(executable_path='./libs/geckodriver')
broswer.get(url)
sleep(4)
CommonUtils.ScrollPageDown(broswer.find_element_by_tag_name('body'), 20)

#response = urllib.request.urlopen(url, timeout=10)
#html = response.read().decode('utf-8')
bs = BeautifulSoup(broswer.page_source, 'lxml')
topAnswers = bs.find_all('meta', attrs={'itemprop': 'url'})
topAnswerUrls = [x.attrs['content'] for x in topAnswers if 'answer' in x.attrs['content']]

fileSeqNo = 0
for url in topAnswerUrls:
    reqAnswer = urllib.request.urlopen(url, timeout=10)  # open answer page
    sleep(2)  # prevent too frequent visiting
    reqAnswerHtml = reqAnswer.read().decode('utf-8')
    answerHtmlBS = BeautifulSoup(reqAnswerHtml, 'lxml')
    title = str.replace(answerHtmlBS.find('title').text, r'/', '') # make it a safe path

    fileSeqNo += 1
    newFile = './spideroutcome/%4d-%s' % (fileSeqNo, title)

    if exists(newFile):
        continue

    with open(newFile, 'x') as fileSaver:
        answerContent = answerHtmlBS.find_all('div', attrs={'class': 'RichContent-inner'})[0]
        answerContent = '<p>Answer URL : {0}</p>'.format(url) + str(answerContent)
        answerContent = '<p>Question : {0}</p>'.format(title) + answerContent

        fileSaver.write(htmlBodyTag.format(answerContent))


