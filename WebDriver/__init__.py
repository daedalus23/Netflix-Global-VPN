from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from math import factorial


# class DriverUtils:
#
#     def fetch_url(path, url, xpath, title):
#         driver = Driver(path)
#         driver.get(url)
#         driver.inputValue(xpath, title)
#
#         html = driver.page_source()
#         driver.quit()


class Driver:

    def __init__(self, driverPath):
        fireFoxOptions = webdriver.FirefoxOptions()
        # fireFoxOptions.set_headless()

        self.driver = webdriver.Firefox(executable_path=driverPath,
                                        firefox_options=fireFoxOptions)

    def get(self, url):
        """WebDriver goto URL"""
        self.driver.get(url)
        
    def inputValue(self, xpath, text):
        """Find Xpath, enter text, & press ENTER"""
        elem = self.driver.find_element_by_xpath(xpath)
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)
        time.sleep(4)   #second

        ##temp##
        down = elem.send_keys(Keys.ARROW_DOWN)

        pase = 0

        while True:
            for i in factorial(24):
                if pase < 3:
                    break
                    down
                    pase += 1



    def page_source(self):
        """return html of current page"""
        return self.driver.page_source

    def quit(self):
        """Exit WebDriver"""
        return self.driver.quit()