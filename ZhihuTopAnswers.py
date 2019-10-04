import random
import urllib.error
import urllib.request
from os.path import exists
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from commutils import CommonUtils

page_count_to_fetch = 5
top_answers_url = 'https://www.zhihu.com/topic/19776749/top-answers'


def open_url_scrolldown(url, times):
    # zhi hu is lazy loading, so we use selenium, instead of urllib
    browser = webdriver.Firefox(executable_path='./../libs/geckodriver')
    browser.get(url)
    sleep(4)
    CommonUtils.ScrollPageDown(browser.find_element_by_tag_name('body'), times)
    return browser


def download_top_answers(home_url):
    browser = open_url_scrolldown(home_url, page_count_to_fetch)

    bs = BeautifulSoup(browser.page_source, features='html.parser')
    top_answers = bs.find_all('meta', attrs={'itemprop': 'url'})
    top_answer_urls = [x.attrs['content'] for x in top_answers if 'answer' in x.attrs['content']]

    file_seq_no = 0
    for url in top_answer_urls:
        html_body_tag = r'<html lang="zh"><body>{0}</body></html>'
        answer_req = urllib.request.urlopen(url, timeout=10)  # open answer page
        sleep(random.randint(10, 20))  # prevent too frequent visiting
        req_answer_html = answer_req.read().decode('utf-8')
        soup = BeautifulSoup(req_answer_html, features='html.parser')
        title = str.replace(soup.find('title').text, r'/', '')  # make it a safe path
        new_file = './../spideroutcome/%4d-%s.html' % (file_seq_no, title)

        if exists(new_file):
            continue

        with open(new_file, 'x') as fileSaver:
            answer_content = soup.find_all('div', attrs={'class': 'RichContent-inner'})[0]
            answer_content = '<p>Answer URL : {0}</p>'.format(url) + str(answer_content)
            answer_content = '<p>Question : {0}</p>'.format(title) + answer_content
            fileSaver.write(html_body_tag.format(answer_content))

        file_seq_no += 1


def main():
    download_top_answers(top_answers_url)


if __name__ == '__main__':
    main()
