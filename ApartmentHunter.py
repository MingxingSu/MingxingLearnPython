import random
import re
import urllib.error
import urllib.request
from os.path import exists
from time import sleep
import requests
from bs4 import BeautifulSoup



house_search_url = r'https://www.idealista.com/en/alquiler-viviendas/madrid/hortaleza/con-precio-hasta_1000,' \
                   r'precio-desde_600,pisos,de-un-dormitorio,de-dos-dormitorios,amueblado_solo-cocina-equipada/'

host_idealist = 'https://www.idealista.com'
headers = { 'Host': 'www.idealista.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'userUUID=257804c4-02f6-4e94-9011-a3564bf95f12; _pxhd=9f75c814157e70bf12fd6924859078f18d5f9ac7d28c90b6194657b4d9dff280:88fd67e0-df7f-11e9-94c3-e32b7cb4660e; xtvrn=$352991$; xtan352991=2-anonymous; xtant352991=1; cto_lwid=283a9987-e2f8-4296-8073-d81f942293b2; utag_main=v_id:016d67f932e000221c561ded54960004c001d0090086e$_sn:3$_ss:1$_st:1569511981029$dc_visit:3$ses_id:1569510181029%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session; cookieDirectiveClosed=true; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22657674f5-e859-4718-ab1c-973b029d57ce%22%2C%22options%22%3A%7B%22end%22%3A%222020-10-26T10%3A30%3A48.640Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-582065-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; _pxvid=88fd67e0-df7f-11e9-94c3-e32b7cb4660e; _hjid=0ea1dd0f-a7b5-45ba-92c1-2e0111ce31dd; TestIfCookieP=ok; pbw=%24b%3d12690%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768; pid=3004253429955223816; pdomid=26; Trk0=Value=253245&Creation=26%2f09%2f2019+17%3a03%3a03; askToSaveAlertPopUp=true; detailFakeAnchorsEffect=true; SESSION=2dca3417-c5b3-4187-9965-1c7e18e1fdc4; WID=ef256b4791da9513|XYzTM|XYzDH; vs=33114=3541863; sasd2=q=%24qc%3D1314772262%3B%24ql%3DMedium%3B%24qpc%3D22463%3B%24qt%3D228_3392_173157t%3B%24dma%3D0&c=1&l=1556374936&lo=-1323644415&lt=637051141823502314&o=1; sasd=%24qc%3D1314772262%3B%24ql%3DMedium%3B%24qpc%3D22463%3B%24qt%3D228_3392_173157t%3B%24dma%3D0; _px2=eyJ1IjoiYmNmNTU1OTAtZTA2ZS0xMWU5LTljY2ItMDkwZGM4YTczMjYyIiwidiI6Ijg4ZmQ2N2UwLWRmN2YtMTFlOS05NGMzLWUzMmI3Y2I0NjYwZSIsInQiOjE1Njk1MTA0ODYzNjIsImgiOiI3YzdmNjNkZmZjNmMyNjllZGNmYWZjNzNiNDhlMGI4NmQzOWEyMDZhMzhiZmQxY2Y5MWEyOTVmN2VmYTY3ODE4In0=; contact2dca3417-c5b3-4187-9965-1c7e18e1fdc4=\"{\'email\':null,\'phone\':null,\'phonePrefix\':null,\'friendEmails\':null,\'name\':null,\'message\':null,\'message2Friends\':null,\'maxNumberContactsAllow\':10,\'defaultMessage\':true}\"; _pxff_tm=1; cookieSearch-1="/alquiler-viviendas/madrid-madrid/con-precio-hasta_1100,precio-desde_600,de-un-dormitorio,de-dos-dormitorios,amueblado_solo-cocina-equipada/:1569510189610',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers'}

def scrap_house_info(url):
    print(url)
    answer_req = requests.get(url, headers= headers)
    sleep(5)
    soup = BeautifulSoup( answer_req.text, features='html.parser')
    houses = soup.find_all('a', attrs={'class': 'item-link'})
    top_answer_urls = [x.attrs['href'] for x in houses]


    for houseUrl in top_answer_urls:
        sleep( random.randint( 5, 10) )
        hou_req = requests.get( host_idealist + houseUrl, headers=headers )
        hou_soup = BeautifulSoup( hou_req.text, features='html.parser' )

        for x in hou_soup.select( selector='.professional-name > div:nth-child(1)'):
            if 'Private owner' in x.text:
                with open('houses.txt', 'a') as fr:
                    print(houseUrl)
                    fr.writelines(host_idealist + houseUrl + '\n')
                    fr.flush()


def scrapPages():
    scrap_house_info(house_search_url)

    page_number = 2
    max_page_count = 2

    while page_number < max_page_count:
        nextPageUrl = '{0}/en/alquiler-viviendas/madrid-madrid/con-precio-hasta_1100,precio-desde_600,' \
                          'de-un-dormitorio,de-dos-dormitorios,amueblado_solo-cocina-equipada/pagina-{1}.htm'.format(host_idealist, page_number)

        scrap_house_info(nextPageUrl)
        page_number +=1
    print('All done!')

def main():
    scrapPages()

if __name__ == '__main__':
    main()
