# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import requests
class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.PhantomJS(service_args=service_args)
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.logger.debug('PhantomJS is Starting')
        page = request.meta.get('page')
        try:
            self.browser.get(request.url)

            num = 2
            for i in range(num):
                sleep(2)
                self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            print(self.browser.page_source)
            body = self.browser.page_source
            #
            # self.browser.implicitly_wait(20)
            # aa = page
            # print(page)
            # input = self.browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div[2]/form/input')
            # input.send_keys(aa)
            # ActionChains(self.browser).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            # self.browser.implicitly_wait(20)
            #
            # # logo = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/div/h3/span')
            # # logo.click()
            #
            # se = {}
            # fensi = self.browser.find_element_by_xpath(
            #     '//*[@id="app"]/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/div/h4[2]')
            # introduce = self.browser.find_element_by_xpath(
            #     '//*[@id="app"]/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/div/h4[1]')
            # se[aa] = [fensi.text, introduce.text]
            # with open("../data/user.txt",'a+',encoding='utf-8') as f:
            #     f.write("#"+aa+"\n")
            #     f.write(fensi.text+" "+introduce.text+"\n")
            return HtmlResponse(url=request.url, body=body, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))


class ProxyMiddleware():
    def __init__(self, proxy_url):
        # self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        if request.meta.get('retry_times'):
            proxy = self.get_random_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                # self.logger.debug('使用代理 ' + proxy)
                request.meta['proxy'] = uri

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )

