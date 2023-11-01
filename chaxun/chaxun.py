def get_telenum(num):
    import requests
    from lxml import etree
    url=f'https://www.ip138.com/mobile.asp?mobile={num}&action=mobile'
    #伪装自己
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60'}

    #发送请求
    resp=requests.get(url,headers=headers)
    #设置中文显示
    resp.encoding='utf-8'
    #解析数据
    e=etree.HTML(resp.text)
    #编写xpath提取数据
    datas=e.xpath('//tbody/tr/td[2]/a/text()')
    #解析响应
    print(datas)

get_telenum(18975437630)


