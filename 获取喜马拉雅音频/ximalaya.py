import requests
import time
import random
import json
import hashlib

#获取音频id链接
url_list='https://www.ximalaya.com/revision/play/v1/show?id=512916473&sort=0&size=30&ptype=1'
#获取标头
headers={'Referer':'https://www.ximalaya.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'}
url_list_resp=requests.get(url_list,headers =headers)

#得到id和名字
track_list=[(track.get('trackId'),track.get('trackName')) for track in url_list_resp.json().get('data').get('tracksAudioPlay')]
for id,name in track_list:
    audio_list=f'https://www.ximalaya.com/revision/play/v1/show?id={id}&sort=0&size=30&ptype=1'
    # print(audio_list)
    # #实现反爬虫
    # #获取服务时间
    # severtime=requests.get('https://www.ximalaya.com/revision/time',headers=headers).text()
    # #现在时间戳
    # nowtime=str(round(time.time()*1000))
    # #求加密参数
    # xm_sign=str(hashlib.md5('himalaya-{}'.format(severtime).encode()).hexdigest())+'({})'.format(round(random.random()*100)+severtime+'({})'.format(round(random.random)*100))+nowtime
    # #更新标头
    # headers['xm_sign']=xm_sign

    resp_src=requests.get(audio_list,headers=headers)
    src=resp_src.json()['data']['src']
    print(src)
