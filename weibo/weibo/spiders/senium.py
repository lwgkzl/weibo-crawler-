# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 21:21 
# @Author : kzl 
# @File : senium.py 
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://m.weibo.cn/p/index?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1554798828&luicode=10000011&lfid=231583')
    driver.implicitly_wait(20)
    logo = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/ul/li[2]/span')
    logo.click()
    driver.implicitly_wait(20)

    all_have = []
    with open("../../data/aa.txt",'r',encoding='utf-8') as f:
        for line in f.readlines():
            if line[0]=='#':
                con = line[1:-2]
                all_have.append(con)

    driver.implicitly_wait(10)
    num = 6
    #加滑动条
    for x in range(num):
        sleep(2)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    tops = driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/h3')
    le = len(tops)
    top_text = [name.text for name in tops]
    print(top_text)
    for i in range(le):
        for x in range(num):
            sleep(3)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        tops = driver.find_elements_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/h3')
        topic_read = driver.find_elements_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/h4[2]')
        print("topic_read",len(topic_read))
        if len(tops)==0:
            print("i find it")
            x = 0
            driver.implicitly_wait(20)
            logo = driver.find_element_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/ul/li[2]/span')
            logo.click()

            for x in range(num):
                sleep(3)
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            tops = driver.find_elements_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/h3')
            topic_read = driver.find_elements_by_xpath(
                '//*[@id="app"]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/h4[2]')
        # print(tops[i].get_attribute(""))
        print(i)
        cao = tops[i].text
        now_con = cao[1:-1]
        #存储每个话题的热度及讨论人数
        with open('../../data/cc.txt','a',encoding='utf-8') as f:
            f.write(now_con+"\n")
            f.write(topic_read[i].text)
            f.write('\n')

        print(now_con)
        if now_con in all_have:
            continue
        all_have.append(now_con)
        ho = [name.text for name in tops]
        topic = tops[i].text
        tops[i].click()
        driver.implicitly_wait(10)
        numm = 100
        # bb = random.randint(5,10)
        for x in range(numm):
            sleep(2)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        names = driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div/div/div/div/div/header/div/div/a/h3')
        hot_name = driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[6]/div/div/div[1]/div/div/header/div/div/a/h3')
        for x in range(len(names)):
            print(names[x].text)
        lle = len(names)
        text = [name.text for name in names]
        with open("../../data/aa.txt","a",encoding="utf-8") as f:
            f.write(topic+"\n")
            for j in range(lle):
                f.write(text[j]+"  ")
            f.write("\n")
        aa = random.randint(3,5)
        sleep(aa)
        driver.back()

