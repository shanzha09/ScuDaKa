# coding = utf-8
"""
author: shanzha
WeChat: work8828
create_time: 2020/12/19 12:58
"""
import requests
import datetime
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

while True:
    timeNow = time.strftime("%H:%M:%S", time.localtime())
    # if True:
    # 部署用，时间改为你想打卡的时间
    if timeNow == "08:30:10":
        today = datetime.date.today()
        date = "%4d%02d%02d" % (today.year, today.month, today.day)
        createTime = round(time.time())

        headers = {
            'Host': 'wfw.scu.edu.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://wfw.scu.edu.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://wfw.scu.edu.cn/ncov/wap/default/index',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
            'Cookie': ''  # chrome复制的放这个引号里面
        }

        data = {
            'date': date,
            'uid': '148083',
            'created': createTime,
            'sfzx': '1',  # 是否在校
            'szxqmc': '望江校区',  # 所在校区 （华西校区， 江安校区， 望江校区）
            'bzxyy': '',  # 不在校原因 （1-6）
            'address': '四川省成都市武侯区望江路街道四川大学四川大学望江校区',
            'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"$Da":"jsonp_303061_","position":{"Q":30.63073,"R":104.08733000000001,"lng":104.08733,"lat":30.63073},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"028","adcode":"510107","businessAreas":[{"name":"小天竺","id":"510107","location":{"Q":30.639354,"R":104.06894199999999,"lng":104.068942,"lat":30.639354}}],"neighborhoodType":"科教文化服务;学校;高等院校","neighborhood":"四川大学","building":"","buildingType":"","street":"望江路","streetNumber":"29号","country":"中国","province":"四川省","city":"成都市","district":"武侯区","township":"望江路街道"},"formattedAddress":"四川省成都市武侯区望江路街道四川大学四川大学望江校区","roads":[],"crosses":[],"pois":[]}',
            'area': '四川省 成都市 武侯区',  # 位置
            'province': '四川省',
            'city': '成都市',
            'zgfxdq': '0',  # 今日是否在中高风险地区？（中高风险地区信息可通过国务院客户端小程序实时查询）
            'tw': '4',  # 体温 （1-9， 1：35℃以下， 2：35℃-36.5℃， 3：36.6℃-36.9℃， 4： 37℃-37.3℃）
            'sfcxtz': '0',  # 今日是否出现发热、乏力、干咳、呼吸困难等症状？
            'sfyyjc': '0',  # 是否到相关医院或门诊检查？
            'sfjcbh': '0',  # 今日是否接触无症状感染/疑似/确诊人群？
            'jcbhlx': '',  # （疑似， 确诊）
            'jcbhrq': '',  # 接触时间
            'mjry': '0',  # 今日是否接触密接人员
            'csmjry': '0',  # 近14日内本人/共同居住者是否去过疫情发生场所（市场、单位、小区等）或与场所人员有过密切接触？
            'sfcyglq': '0',  # 是否处于观察期？
            'gllx': '',  # 观察场所 （1—4）
            'glksrq': '',  # 观察开始时间
            'sfjxhsjc': '0',  # 2020年9月1日（含）后是否进行过新冠肺炎核酸检测？
            'hsjcrq': '',  # 核酸检测时间
            'hsjcdd': '',  # 核酸检测地点
            'hsjcjg': '0',  # 核酸检测结果 （0-2）
            'sfcxzysx': '0',  # 是否有任何与疫情相关的， 值得注意的情况？
            'qksm': '',  # 情况说明
            'jcjgqr': '0',
            'remark': '',
            'sfjcwhry': '0',
            'sfjchbry': '0',
            'bztcyy': '5',
            'sftjhb': '0',
            'sftjwh': '0',
            'szcs': '',
            'szgj': '',
            'jcjg': '',
            'jcqzrq': '',
            'sfjcqz': '',
            'szsqsfybl': '0',
            'sfsqhzjkk': '0',
            'sqhzjkkys': '',
            'sfygtjzzfj': '0',
            'gtjzzfjsj': '',
            'fxyy': '学习',
            'id': '22500922',
            'gwszdd': '',
            'sfyqjzgc': '',
            'jrsfqzys': '',
            'jrsfqzfy': '',
            'szgjcs': '',
            'ismoved': '0'
        }

        response = requests.post(url='https://wfw.scu.edu.cn/ncov/wap/default/save', headers=headers, data=data)
        logging.info(response.status_code)
        logging.info(response.json())
        time.sleep(82800)
