from urllib.request import quote, unquote
import random
import requests
import json
import traceback
# keyword = quote('java').strip()
# print(keyword, type(keyword))
# city = quote('郑州').strip()
# print(unquote(city))
import time
import os
refer_url1 = 'http://newzspt.p5w.net/bbs/bbs.asp?boardid=3902'
refer_url2 = 'http://rs.p5w.net/html/106029.shtml'
refer_url3 = 'http://ircs.p5w.net/ircs/topicInteraction/bbs.do?rid=18403'
ajax_url = 'http://rs.p5w.net/roadshowLive/getNInteractionDatas.shtml'
two_ajac = 'http://ircs.p5w.net/ircs/topicInteraction/questionPage.do'
three_ajac = 'http://newzspt.p5w.net/bbs/question_page.asp?boardid=3902&bbs=1&pageNo=4&now=2314'
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
]

path = './data/'
if not os.path.exists(path):
    os.mkdir(path)

import xml.etree.ElementTree as ET
# def get_tagname():




def get_result(refer_url,ajax_url,page,roadshowid):
    data = {
        'roadshowId': roadshowid,
        'isPagination': '1',
        'rows': '10',
        'type': '2',
        'page': page
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'rs.p5w.net',
        'Origin': 'http://rs.p5w.net',
        'Referer': refer_url,
        'User-Agent': user_agents[random.randrange(0, 4)],
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
    }
    resp = requests.post(ajax_url, data=data, headers=headers)
    result = resp.json()
    return result


# def get_result():
#     pageNo
#     10
#     rid
#     14272

def get_result2(refer_url,ajax_url,page,pid):
    data = {
        'pageNo': page,
        'rid': pid,
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'ircs.p5w.net',
        'Referer': refer_url,
        'User-Agent': user_agents[random.randrange(0, 4)],
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
    }
    resp = requests.post(ajax_url, data=data, headers=headers)
    # print(resp)
    result = resp.json()
    # print("*"*15)
    # print(result)
    aa = json.loads(result['value'])
    return aa

def solve_str(s):
    return s.replace(" ","").replace('\n','')
from lxml import etree
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
def get_result4(page,pid):
    web_id = "http://zsptbs.p5w.net/bbs/chatbbs/left.asp?boardid={}&fsize=2&pageNo={}".format(pid,page)
    resp = requests.get(web_id)
    soup = BeautifulSoup(resp.content.decode('gbk'), 'lxml')
    # print(soup.find_all('tr'))
    aa = soup.find_all('tr')
    peo_list = []
    sen_list = []
    flag = 0
    for a in aa:
        bb = list(a.find_all('td'))
        if len(bb) >=4:
            # print(type(bb[1].string),bb[1].string)
            # print(bb[0].string,bb[1].string)
            # print("hello")
            # print(str(bb[2].string),page)
            if "主持人" in str(bb[2].string) and page > 1:
                flag = 1
            if str(bb[1].string).strip() != "":
                c = list(bb[3])
                if len(c) > 1:
                    peo = solve_str(str(bb[2].string))
                    sen = solve_str(str(c[1].string))
                    if peo is  not None and len(sen) > 5:
                        peo_list.append(peo)
                        sen_list.append(sen)
    return peo_list,sen_list,flag
            # print(c)
            # for c in bb[3]:
            #     print(c.string)
# get_result4(refer_url1,1,572)



def get_four_page(refer_url,roadid):
    onepage_peo, onepage_sen = [], []
    for page in range(1,20):
        # print(page)
        if page < 2:
            print(refer_url)
        time.sleep(1)
        flag = 0
        try:
            peo, sen, flag = get_result4(page,roadid)
            onepage_peo.extend(peo)
            onepage_sen.extend(sen)
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            print(refer_url,page)
        # if len(peo) != len(sen):
        #     print("peo and sen don't have equal length!")
        #     continue

        if flag == 1:
            break
        # time.sleep(2)
    # print(len(onepage_peo),onepage_peo[0])
    return onepage_peo, onepage_sen

# aa,bb = get_four_page("aa",572)
# for i,b in enumerate(aa):
#     print(aa[i],bb[i])


def get_result3(refer_url,ajax_url,page,pid):
    data = {
        'pageNo': page,
        'boardid': pid,
        'bbs':1,
        'now':1568995955886
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'newzspt.p5w.net',
        'Referer': refer_url,
        'User-Agent': user_agents[random.randrange(0, 4)],
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
    }
    resp = requests.post(ajax_url, data=data, headers=headers)
    resp.encoding = 'gbk'
    aa = resp.text
    # print(aa)
    # print(type(aa))
    # aa.replace("gbk","utf-8")
    # with open('aa.xml','wb') as f:
    #     f.write(aa)
    bb = ET.fromstring(aa)
    peo,sen = [],[]
    flag = 0
    for ta in bb:
        name = ""
        context = ""
        # print(ta.tag)
        if len(ta)>0 :
            # if page == 6:
            #     print(ta[0][1].text)
            if "主持人" in ta[0][1].text and page > 1:
                # print("yes")
                flag = 1
        if len(ta) < 2:
            continue
        for ch in ta[1]:
            if ch.tag == "r_officename":
                name = ch.text
                # print(name)
            if ch.tag == "r_content":
                context = ch.text
        peo.append(name)
        sen.append(solve_str(context))
    return peo,sen,flag
    # with open("aa.txt",'w',encoding='utf-8') as f:
    #     for i,p in enumerate(peo):
    #         f.write(str(p)+": ")
    #         f.write(str(sen[i])+"\n")
    # print(type(resp))
    # result = resp.xml()
    # print(type(result))
    # aa = json.loads(result['value'])
    # return result
# for i in range(1,10):
#     aj = 'http://newzspt.p5w.net/bbs/question_page.asp?boardid={}&bbs=1&pageNo={}&now=2314'.format(3902,i)
#     a,b,c = get_result3(refer_url1,aj,i,3902)
#     print(i)
#     if c==1:
#         break
def load_json2(result,page):
    aa = result['q_all']
    le = len(aa)
    peo,sen = [], []
    flag = 0
    for i in range(le):
        name = ""
        cont = ""
        if page > 1 and "主持人" in aa[i]['q_jblb']:
            flag = 1
        if 'q_jblb' in aa[i].keys() and 'q_content' in aa[i].keys() and "主持人" not in aa[i]['q_jblb']:
            if "董事长" in aa[i]['q_jblb'] or "总经理" in aa[i]['q_jblb'] or "各位投资者" in aa[i]['q_content']:
                peo.append(aa[i]['q_jblb'])
                sen.append(solve_str(aa[i]['q_content']))
        if 'reply' in aa[i].keys():
            if aa[i]['reply'][0]['r_officename'] != None:
                name = name + aa[i]['reply'][0]['r_officename']
            if aa[i]['reply'][0]['r_content'] != None:
                cont = cont + aa[i]['reply'][0]['r_content']
        peo.append(name)
        sen.append(solve_str(cont))
    lle = len(peo)
    # for i in range(lle):
    #     print(peo[i],sen[i])
    return peo,sen,flag

def load_json(result):
    people,sen = [],[]
    # print(len(result['rows']))
    le = len(result['rows'])
    # print(result['rows'][-2]['speakContent'])
    for i in range(le):
        # people.append(result['rows'][i]['replyList'])
        aa = result['rows'][i]['replyList']
        # if "投资者" in result['rows'][i]['speakContent']:
        #     print(result['rows'][i]['speakContent'])
        if "主持人" not in result['rows'][i]['speakUserName'] and "各位投资者" in result['rows'][i]['speakContent']:
            people.append(result['rows'][i]['speakUserName'])
            sen.append(solve_str(result['rows'][i]['speakContent']))
            return people,sen,1
        aa_len = len(aa)
        for j in range(aa_len):
            if aa[j]['speakContent'] != "":
                people.append(aa[j]['speakUserName'])
                sen.append(solve_str(aa[j]['speakContent']))
    zh = len(people)
    # for i in range(zh):
    #     print(people[i],sen[i])
    return people,sen,0

def get_three_page(refer_url,roadid):
    onepage_peo, onepage_sen = [], []
    for page in range(1,15):
        # print(page)
        if page < 2:
            print(refer_url)
        time.sleep(1)
        flag = 0
        ajaxurl3 = 'http://newzspt.p5w.net/bbs/question_page.asp?boardid={}&bbs=1&pageNo={}&now=2314'.format(roadid,page)
        try:
            peo, sen, flag = get_result3(refer_url,ajaxurl3,page,roadid)
            onepage_peo.extend(peo)
            onepage_sen.extend(sen)
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            print(refer_url,page)
        # if len(peo) != len(sen):
        #     print("peo and sen don't have equal length!")
        #     continue

        if flag == 1:
            break
        # time.sleep(2)
    # print(len(onepage_peo),onepage_peo[0])
    return onepage_peo, onepage_sen
# a,b = get_three_page("http://newzspt.p5w.net/bbs/bbs.asp?boardid=3737",3737)
# for i,v in enumerate(a):
#     print(v+": "+b[i])

def get_one_page(refer_url,ajax_url,roadid):
    onepage_peo, onepage_sen = [], []
    for page in range(100):
        # print(page)
        if page < 2:
            print(refer_url)
        result = get_result(refer_url,ajax_url,page,roadid)
        time.sleep(1)
        if len(result['rows']) == 0:
            break
        peo,sen = [], []
        flag = 0
        try:
            peo, sen, flag = load_json(result)
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            print(refer_url,page)
        if len(peo) != len(sen):
            print("peo and sen don't have equal length!")
            continue
        onepage_peo.extend(peo)
        onepage_sen.extend(sen)
        if flag == 1:
            break
        # time.sleep(2)
    # print(len(onepage_peo),onepage_peo[0])
    return onepage_peo, onepage_sen
# print(result)


def get_two_page(refer_url,ajax_url,roadid):
    onepage_peo, onepage_sen = [], []
    for page in range(1,15):
        # print(page)
        if page < 2:
            print(refer_url)
        result = get_result2(refer_url,ajax_url,page,roadid)
        time.sleep(1)
        if len(result['q_all']) == 0:
            break
        peo,sen = [], []
        flag = 0
        try:
            peo, sen,flag = load_json2(result,page)
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            print(refer_url,page)
        if len(peo) != len(sen):
            print("peo and sen don't have equal length!")
            continue
        onepage_peo.extend(peo)
        onepage_sen.extend(sen)
        if flag == 1:
            break
        # time.sleep(2)
    print(len(onepage_peo),onepage_peo[0])
    return onepage_peo, onepage_sen

# def get_four_page(refer_url,roadid):
#     pass


def get_all_page(source_url,page):
    data = {
        'perComType':	0,
        'roadshowType':	5,
        'companyType':None,
        'roadshowDate':None,
        'page':	page,
        'rows':	12
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'rs.p5w.net',
        'Origin': 'http://rs.p5w.net',
        'Referer': 'http://rs.p5w.net/roadshow?roadshowType=5',
        'User-Agent': user_agents[random.randrange(0, 4)],
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
    }
    resp = requests.post(source_url, data=data, headers=headers)
    result = resp.json()
    le = len(result['rows'])
    for i in range(le):
        try:
            code = result['rows'][i]['companyCode']
            name = result['rows'][i]['roadshowTitle']
            ttime = result['rows'][i]['roadshowDateFinish']

            roadid = result['rows'][i]['pid']
            lastname = code
            if lastname == None:
                lastname = ""
            if name != None:
                lastname += name
            if ttime != None:
                lastname += ttime
            if result['rows'][i]['roadshowActiveHis'] == None:
                roadshow = result['rows'][i]['roadshowUrl']
                roadshoeurl = 'http://rs.p5w.net/' + roadshow   #roadshowActiveHis
                peo, sen = get_one_page(roadshoeurl, ajax_url, roadid)
            elif "newzspt" not in result['rows'][i]['roadshowActiveHis'] and "zsptbs" not in result['rows'][i]['roadshowActiveHis']:
                roadshoeurl = result['rows'][i]['roadshowActiveHis']
                peo, sen = get_two_page(roadshoeurl, two_ajac, roadid)
            elif "newzspt" in result['rows'][i]['roadshowActiveHis']:
                roadshoeurl = result['rows'][i]['roadshowActiveHis']
                indexx = roadshoeurl.rindex('=') + 1
                roadid = roadshoeurl[indexx:]
                peo,sen = get_three_page(roadshoeurl,roadid)
            elif "zsptbs" in result['rows'][i]['roadshowActiveHis']:
                roadshoeurl = result['rows'][i]['roadshowActiveHis']
                indexx = roadshoeurl.rindex('=')+1
                roadid = roadshoeurl[indexx:]
                peo,sen = get_four_page(roadshoeurl,roadid)
            # print(roadshoeurl)
            file_path = os.path.join(path, lastname+ ".txt")
            xxlen = min(len(peo), len(sen))
            time.sleep(3)
            with open(file_path, 'a+', encoding='utf-8') as f:
                for x in range(xxlen):
                    if peo[x] == None:
                        peo[x] = "无名"
                    if sen[x] == None:
                        sen[x] = ""
                    f.write(str(peo[x]) + " : " + str(sen[x]) + "\n")
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            # print("error: ",roadshoeurl)

# aa,bb=get_three_page("http://newzspt.p5w.net/bbs/bbs.asp?boardid=45",45)
# for i,v in enumerate(aa):
#     print(aa[i],bb[i])

#待做事项：1.将所有跑异常的网址存下来，准备复查，2.将


def main():
    first_page = 'http://rs.p5w.net/roadshow/getRoadshowList.shtml'
    for i in range(884,1063):
        print(i,'*'*25)
        get_all_page(first_page,i)


    # print(result)
# result 就是最终获得的json格式数据
# item = result['content']['positionResult']['result'][0]
# print(item)
# item就是单个招聘条目信息
# result = get_result(refer_url,ajax_url,10)
# print(result)
# peo ,sen = get_one_page(refer_url,ajax_url)
# for k,v in enumerate(peo):
#     print(str(peo[k])+": "+str(sen[k]))
# load_json(result)
# main()
# p,s = get_two_page(refer_url1, two_ajac, 18346)
# for k,b in enumerate(p):
#     print(p[k],s[k])
# peo,sen = get_two_page(refer_url3,two_ajac,18403)
# for i,v in enumerate(peo):
#     print(v,sen[i])
print("程序结束")
#
# re = get_one_page(refer_url1,ajax_url,'000159810378FC164CD59F550A87CB9821FA')
# print(re)
# rer = get_one_page(refer_url2,ajax_url,'000190A0164093D644A8936620BFD4B767B1')
# print(rer)
