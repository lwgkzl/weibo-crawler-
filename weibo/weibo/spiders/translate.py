# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 11:18 
# @Author : kzl 
# @File : translate.py 
class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = '_T_WM=8740b56714f8401f199f4d96b1082036; ALF=1557384153; SCF=Ai5Ur3xinPGQKkumCY1_xP0aoyFTJnsEgIPHZtTbNrj8fVzqR5rIKJf6Po6PuvOSpm5kEzgADBo7Tje45hcfV0M.; SUB=_2A25xqE-YDeRhGeNJ7lMW8CfFwjmIHXVTU1HQrDV6PUJbktANLXPskW1NS9aIjDcttp0mUFH0EwUcHoJ4bMO5IObK; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5p3rcEA3_8jXVOmjY7SF035JpX5K-hUgL.Fo-NSK2Neh.41K-2dJLoIEBLxK-LBo5L12qLxKMLBK.LB.2LxKBLBonLB-BLxKqLBK-LB.et; SUHB=0FQ7abNi9gB6sK; SSOLoginState=1554792392; MLOGIN=1; WEIBOCN_FROM=1110106030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231583%26fid%3D106003type%253D25%2526t%253D3%2526disable_hot%253D1%2526filter_type%253Dtopicband%26uicode%3D10000011; XSRF-TOKEN=ad554f'
    trans = transCookie(cookie)
    print(trans.stringToDict())
