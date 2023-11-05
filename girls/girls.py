#地址

url='http://www.netbian.com/mei/'

#发送请求
#导入解析xpath的工具lxml
from lxml import etree
import requests

resp=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'})
resp.encoding='gbk'#中文显示
#print(resp.text)
e=etree.HTML(resp.text)

#提取图片地址
img_urls=e.xpath('//ul/li/a/img/@src')
img_names=e.xpath('//ul/li/a/img/@alt')

#保存数据
for n,u in zip(img_names,img_urls):
    print(f'正在下载：图片名：{n}')
    img_resp=requests.get(u,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'})
    with open(f"D:\\python\python实战案例\girls\img_f\{n}.jpg","wb") as f:
        f.write(img_resp.content)


