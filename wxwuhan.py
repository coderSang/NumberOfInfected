# coding:utf-8
# 导入模块
from wxpy import *
import requests
import json
import time

# 初始化机器人，扫码登陆
bot = Bot()
# 搜索名称好友
my_friend = bot.friends().search('我是一个猪头三')[0]
oldValue = oldCureNum = oldDeathNum = oldValueH = oldCureNumH = oldDeathNumH = 0


def getDataHistory():
    url = 'https://interface.sina.cn/news/wap/fymap2020_data.d.json'
    r = requests.request('post', url)
    d = json.loads(r.text)
    for i in range(len(d["data"]["list"])):
        if d["data"]["list"][i]["name"] == "浙江":
            my_friend.send(d["data"]["list"][i]["name"] + ":" +
                           "总数:" + d["data"]["list"][i]["value"] +
                           "治愈:" + d["data"]["list"][i]["cureNum"] +
                           "死亡:" + d["data"]["list"][i]["deathNum"]
                           )
            for j in range(len(d["data"]["list"][i]["city"])):
                if d["data"]["list"][i]["city"][j]["name"] == "湖州":
                    my_friend.send(d["data"]["list"][i]["city"][j]["name"] + ":" +
                                   "总数:" + d["data"]["list"][i]["city"][j]["conNum"] +
                                   "治愈:" + d["data"]["list"][i]["city"][j]["cureNum"] +
                                   "死亡:" + d["data"]["list"][i]["city"][j]["deathNum"]
                                   )


if __name__ == "__main__":
    getDataHistory()
    while True:
        time.sleep(60*60*3)
        getDataHistory()
