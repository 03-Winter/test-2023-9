import requests
from lxml import etree
for i in range(1,4):
    #发送请求
    resp=requests.get(f'https://newhouse.fang.com/house/s/b9{i}/')
    #设置格式
    resp.encoding='utf-8'
    #解析数据
    e=etree.HTML(resp.text)
    names=[n.strip() for n in e.xpath('//div[@class="nlcd_name"]/a/text()')]
    # print(names)
    address=e.xpath('//div[@class="address"]/a/@title')
    # print(address)
    comment=[c for c in e.xpath('//div[@class="fangyuan"]/a[1]/text()')]
    # print(comment)
    price=[p.xpath('string(.)').strip() for p in e.xpath('//div[@class="nhouse_price"]')]
    # print(price)
    data=[]
    for n,a,c,p in zip(names,address,comment,price):
        data.append([n,a,p])
    # print(f'{n}=={a}=={c}=={p}')

import pandas
# with open('房子数据.txt','w',encoding='utf=8') as f:
df=pandas.DataFrame(data,columns=['小区名','地址','价格'])
print(df)




