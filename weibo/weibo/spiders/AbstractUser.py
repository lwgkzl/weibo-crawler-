# -*- coding: utf-8 -*- 
# @Time : 2019/4/10 22:07 
# @Author : kzl 
# @File : AbstractUser.py 
import json
def get_user():
    all_user = []
    se = {}
    with open("../../data/bb.txt",'r',encoding='utf-8') as f:
        for line in f.readlines():
            if line[0]!='#':
                cu = line.split()
                all_user.extend(cu)
    all_user = list(set(all_user))
    se['user'] = all_user
    with open('../../data/user.json','w',encoding='utf-8') as f:
        json.dump(se,f)
        print("all user1 dump complete!")
    with open('../../data/beifen.json','w',encoding='utf-8') as f:
        json.dump(se,f)
        print("all user2 dump complete!")
    return all_user

# all=get_user()
# # print(all)
# print(len(all))

def get_json():
    with open('../../data/user.json','r',encoding='utf-8') as f:
        se = json.load(f)
        print("data load")
    return se['user']

# all = get_json()
# for i in all:
#     print(i)

def divede():
    with open('../../data/user2.json','r',encoding='utf-8') as f:
        se = json.load(f)
        print("data load")
    all_user =  se['user']
    have = []
    with open('../../data/user2.txt','r',encoding="utf-8") as f:
        for line in f.readlines():
            if line[0]=='#':
                have.append(line[1:-1])
    print(have)
    with open('../../data/bad2.txt','r',encoding="utf-8") as f:
        for line in f.readlines():
            have.append(line[:-1])
    last = [i for i in all_user if i not in have]
    print(last)
    print(len(last))
    le = int(len(last)/3)
    lle = le*2
    last1 = last[:le]
    last2 = last[le:lle]
    last3 = last[lle:]
    se1 = {}
    se2 = {}
    se3 = {}
    se1['user'] = last1
    se2['user'] = last2
    se3['user'] = last3
    with open('../../data/user31.json','w',encoding='utf-8') as f:
        json.dump(se1,f)
    with open('../../data/user32.json','w',encoding='utf-8') as f:
        json.dump(se2,f)
    with open('../../data/user33.json','w',encoding='utf-8') as f:
        json.dump(se3,f)

    with open('../../data/user31.json','r',encoding='utf-8') as f:
        ss = json.load(f)
        print(ss)
    with open('../../data/user32.json','r',encoding='utf-8') as f:
        sss = json.load(f)
        print(sss)
    with open('../../data/user33.json','r',encoding='utf-8') as f:
        ss = json.load(f)
        print(ss)

# divede()

def get_topic_with_user():
    se = {}
    with open("../../data/aa.txt",'r',encoding='utf-8') as f:
        aa = "null"
        for line in f.readlines():
            if line[0]!='#':
                cu = line.split()
                if aa in se.keys():
                    cu.extend(se[aa])
                set_u = list(set(cu))
                se[aa] = set_u
            else:
                aa = line[1:-2]
    del_topic = []
    al_user = {}
    with open('../../data/all_user.json','r',encoding='utf-8') as f:
        al_user = json.load(f)
    num = 0
    for i,j in se.items():
        if len(j)<50:
            # print(i,len(j))
            del_topic.append(i)
        else:
            for u in j:
                if u not in al_user.keys():
                    num = num + 1
                    j.remove(u)
    print("user:",num)
    for i in del_topic:
        print(i)
        se.pop(i)
    print(len(se))
    # with open('../../data/TopicWithUser.json','w',encoding='utf-8') as f:
    #     json.dump(se,f)
    #     print("file dump complete")

def check_topic_with_user():
    se = {}
    with open('../../data/TopicWithUser.json','r',encoding='utf-8') as f:
        se = json.load(f)
        print("file load complete")
        print(se)
        print(len(se))
        for i,j in se.items():
            print(i,len(j))

def get_all_user_from_user():
    se = {}
    with open("../../data/user.txt",'r',encoding='utf-8') as f:
        aa = ""
        for line in f.readlines():
            if line[0]=='#':
                aa = line[1:-1]
            else:
                se[aa] = line[:-1]
        print(se)
    with open('../../data/all_user.json','w',encoding='utf-8') as f:
        json.dump(se,f)




if __name__ == '__main__':
    # get_all_user_from_user()
    get_topic_with_user()