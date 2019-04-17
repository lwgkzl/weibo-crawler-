# -*- coding: utf-8 -*- 
# @Time : 2019/4/10 21:33 
# @Author : kzl 
# @File : second_seleinum.py 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import  random
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
PROXIES = [
    {'ip_port': '182.101.1.35:48608', 'user_pass': ''},
    {'ip_port': '182.101.1.85:48608', 'user_pass': ''},
    {'ip_port': '182.84.227.4:46806', 'user_pass': ''},
    {'ip_port': '182.84.227.14:46806', 'user_pass': ''},
]
def get_one_user(content):
    random_num = random.randint(0, 1)
    proxy = PROXIES[random_num]['ip_port']
    Firefox_options = webdriver.FirefoxOptions()
    Firefox_options.add_argument('--proxy-server=http://' + proxy)
    Firefox_options.add_argument('-headless')
    # chrome = webdriver.Chrome(chrome_options=chrome_options)
    drive = webdriver.Firefox(firefox_options=Firefox_options)
    try:
        drive.get('https://m.weibo.cn/search?containerid=231583')
        drive.implicitly_wait(10)
        aa = content
        print(content)
        input = drive.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div[2]/form/input')
        input.send_keys(aa)
        ActionChains(drive).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        drive.implicitly_wait(10)

        user_button = drive.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[2]/span')
        drive.implicitly_wait(10)
        user_button.click()
        se = {}
        fensi = drive.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]/div/div/div/div[2]/div/h4[2]')
        introduce = drive.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[1]/div/div/div/div[2]/div/h4[1]')
        se[aa] = [fensi.text, introduce.text]
        with open("../../data/user31.txt", 'a+', encoding='utf-8') as f:
            f.write("#" + aa + "\n")
            f.write(fensi.text + " " + introduce.text + "\n")
        drive.quit()
    except NoSuchElementException:
        with open("../../data/bad31.txt","a+",encoding="utf-8") as f:
            f.write(content+"\n")
        print(content+"not find")
        drive.quit()
    except WebDriverException:
        with open("../../data/bad31.txt","a+",encoding="utf-8") as f:
            f.write(content+"\n")
        print("net work is not good")
        sleep(8)
        drive.quit()
if __name__ == '__main__':
    with open(r'F:\PycharmProjects\weibo\data\user31.json','r',encoding='utf-8') as f:
        se = json.load(f)
        print("data load")
    print(len(se))
    cu = []
    for i in se['user']:
        if i in cu:
            continue
        sleep(3)
        get_one_user(content=i)