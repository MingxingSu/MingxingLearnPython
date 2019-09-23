from time import sleep
from selenium.webdriver.common.keys import Keys


class CommonUtils:

    @staticmethod
    def ScrollPageDown(page, times):
        while times:
            page.send_keys(Keys.PAGE_DOWN)
            sleep(3)
            times -= 1