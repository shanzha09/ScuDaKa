import requests
import datetime
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

while True:
    timeNow = time.strftime("%H:%M:%S", time.localtime())
    if True:
    # 部署用，时间改为你想打卡的时间
    #if timeNow == "07:30:10":
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
            'Cookie': 'eai-sess=; UUkey=;'  # chrome复制的放这个引号里面
        }
        data={
            'zgfxdq': '0',
            'mjry': '0',
            'csmjry': '0',
            'szxqmc': '江安校区',
            'sfjzxgym': '1',
            'jzxgymrq': '2021-08-02',
            'sfjzdezxgym': '1',
            'jzdezxgymrq': '2021-08-30',
            'sfjzdszxgym': '0',
            'jzdszxgymrq': '',
            'tw': '3',
            'sfcxtz': '0',
            'sfjcbh': '0',
            'sfcxzysx': '0',
            'qksm': '',
            'sfyyjc': '0',
            'jcjgqr': '0',
            'remark': '',
            'address': '四川省成都市双流区西航港街道环行大道西段四川大学江安校区体育学院',
            'geo_api_info': '{"type":"complete","position":{"Q":30.552599826389,"R":103.99560655381998,"lng":103.995607,"lat":30.5526},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":69,"isConverted":true,"status":1,"addressComponent":{"citycode":"028","adcode":"510116","businessAreas":[{"name":"白家","id":"510116","location":{"Q":30.562482,"R":104.006821,"lng":104.006821,"lat":30.562482}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"川大路二段","streetNumber":"1号","country":"中国","province":"四川省","city":"成都市","district":"双流区","towncode":"510116002000","township":"西航港街道"},"formattedAddress":"四川省成都市双流区西航港街道环行大道西段四川大学江安校区体育学院","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
            'area': '四川省 成都市 双流区',
            'province': '四川省',
            'city': '成都市',
            'sfzx': '1',
            'sfjcwhry': '0',
            'sfjchbry': '0',
            'sfcyglq': '0',
            'gllx': '',
            'glksrq': '',
            'jcbhlx': '',
            'jcbhrq': '',
            'bztcyy': '1',
            'sftjhb': '0',
            'sftjwh': '0',
            'szcs': '',
            'szgj': '',
            'bzxyy': '',
            'jcjg': '',
            'hsjcrq': '',
            'hsjcdd': '',
            'hsjcjg': '0',
            'date': date,
            'uid': '3302657',
            'created': createTime,
            'jcqzrq': '',
            'sfjcqz': '',
            'szsqsfybl': '0',
            'sfsqhzjkk': '0',
            'sqhzjkkys': '',
            'sfygtjzzfj': '0',
            'gtjzzfjsj': '',
            'fxyy': '开学',
            'id': '69928984',
            'gwszdd': '',
            'sfyqjzgc': '',
            'jrsfqzys': '',
            'jrsfqzfy': '',
            'szgjcs': '',
            'ismoved': '0'}
        response = requests.post(url='https://wfw.scu.edu.cn/ncov/wap/default/save', headers=headers, data=data)
        logging.info(response.status_code)
        logging.info(response.json())
        time.sleep(82800)
