import requests
from lxml import etree
#发送请求
url='https://datachart.500.com/ssq/'
#伪装自己
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

resp=requests.get(url,headers=headers)
#设置中文编码
resp.encoding='gbk'
# print(resp.text)
e= etree.HTML(resp.text)
redball=[tr.xpath('./td[contains(@class,"chartBall01")]/text()') for tr in e.xpath('//tbody[@id="tdata"]/tr[not(contains(@class,"tdbck"))]')]
print(redball)
blueball=e.xpath('//tbody[@id="tdata"]/tr[not(contains(@class,"tdbck"))]/td[contains(@class,"chartBall02")]/text()')

with open('caipiao.txt', 'w', encoding='utf-8') as f:
    for r,b in zip(redball,blueball):
        f.write(f'红球号码：{r}，蓝球号码：{b}\n')


