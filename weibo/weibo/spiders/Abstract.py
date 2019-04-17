# -*- coding: utf-8 -*- 
# @Time : 2019/4/11 20:54 
# @Author : kzl 
# @File : Abstract.py 
import json

path = r"F:\PycharmProjects\weibo\data\TopicWithUser.json"   #此处修改路径
def check_topic_with_user(path):
    se = {}
    with open(path,'r',encoding='utf-8') as f:
        se = json.load(f)
        print("file load complete")
    for i,j in se.items():
        print(i)
        print(j)

user_path = r'F:\PycharmProjects\weibo\data\all_user.json'  #此处修改路径
def get_all_user():
    se = {}
    with open(user_path,'r',encoding='utf-8') as f:
        se = json.load(f)
        print("file load complete")
    print("有"+str(len(se))+"个用户")
    for i,j in se.items():
        print(i,j)

#需要查看那个，就解除注释
#查看话题以及话题下的用户
# check_topic_with_user()

#查看用户的粉丝数
get_all_user()