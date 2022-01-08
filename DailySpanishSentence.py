from email.header import Header
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from my_html_parser import MyHtmlParser
from mail import EmailUtils

class DailySentence:

    @staticmethod
    def get_daily_sentence():
        url = 'http://www.esdict.cn/home/dailysentence'
        req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = urllib.request.urlopen( req )
        html = con.read().decode('utf-8')
        

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
                #EmailUtils.send_from_gmail_to_my_workemail(subject, msg.encode('utf-8'))




def main():
    DailySentence.get_daily_sentence()


if __name__ == '__main__':
    main()







