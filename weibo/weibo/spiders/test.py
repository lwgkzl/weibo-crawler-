# -*- coding: utf-8 -*- 
# @Time : 2019/4/11 22:08 
# @Author : kzl 
# @File : test.py 
from selenium import webdriver

#检测代理是否可用
proxy = '182.101.1.45:48608'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://httpbin.org/get')
# Chrome_options = webdriver.ChromeOptions()
# Chrome_options.add_argument('-headless')
# drive = webdriver.Chrome(chrome_options=Chrome_options)
# drive.get('http://httpbin.org/get')
# print(drive.page_source)