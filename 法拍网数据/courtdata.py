import requests
from lxml import etree
form_data={
'type':'1',
'name':'',
'area':'北京市',
'city':'北京市',
'city1':'==请选择==',
'city2':'==请选择==',
'xmxz':'1',
'state':'2',
'money':'',
'money1':'',
'number':'0',
'fid1':'',
'fid2':'',
'fid3':'',
'order':'0',
'page':'1',
'include':'0',
}
headers={
    'Cookie':'__jsluid_s=db77a455d8f5f76b34fbdd6db68c0fdb; __jsl_clearance_s=1697802187.132|0|kCDn3%2BjLQx9Ix8B8scq1Mzi2Vuc%3D; ASP.NET_SessionId=b0k35bhff2yyob55g3ix2a02; Cookies-01=76891161',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
    'Referer':'https://www1.rmfysszc.gov.cn/projects.shtml?x=1&s=2&o=3'
}
#发送请求
resp=requests.get("https://www1.rmfysszc.gov.cn/projects.shtml?x=1&s=2&o=3",headers=headers,)


print(resp.text)
e=etree.HTML(resp.text)
#提取标题
title=e.xpath('//div[@class="product"]/div[@class="p_img"]/a/@title')


#提取价格
price1=e.xpath('//div[@class="prod-guj"]/p[1]/strong/text()')#
price2=e.xpath('//div[@class="prod-guj"]/p[2]/span/text()')#评估价起拍价
#处理数据
print(price1)
#for t,i,p1,p2 in zip(title,)


#查看结果
print(resp.text)

#


