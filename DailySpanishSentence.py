import urllib.error
import urllib.request
from bs4 import BeautifulSoup
from MyHtmlParser import MyHtmlParser
from mail import EmailUtils

class DailySentence:

    @staticmethod
    def get_daily_sentence():
        url = 'http://www.esdict.cn/home/dailysentence'

        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"}

        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode('utf-8')

        # Use my html parser to  get all data
        html_parser = MyHtmlParser()
        html_parser.feed(html)

        data = html_parser.HTMLData
        html_parser.clean()

        # Use BS to find element
        bs = BeautifulSoup(html,features='html.parser')
        tran = bs.find('p', attrs={'class': 'sect-trans'})

        for line in data:
            if line[:4] == '每日一句':
                print(line)
                print(tran.text)

                #send email
                subject = 'Daily Spanish Sentence'
                msg = line + '\n' + tran.text
                EmailUtils.send_from_gmail_to_my_workemail(subject, msg.encode('utf-8'))




def main():
    DailySentence.get_daily_sentence()


if __name__ == '__main__':
    main()







