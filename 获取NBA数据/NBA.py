import requests
url='https://nba.hupu.com/stats/players'
headers={'User-Agent':'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}
resp=requests.get(url,headers=headers)

from lxml import etree

e=etree.HTML(resp.text)
ranking=e.xpath('//table[@class="players_table"]/tbody/tr/td[1]/text()')
names=e.xpath('//table[@class="players_table"]/tbody/tr/td[2]/a/text()')
teams=e.xpath('//table[@class="players_table"]/tbody/tr/td[3]/a/text()')
score=e.xpath('//table[@class="players_table"]/tbody/tr/td[4]/text()')

with open('nba.txt','w',encoding='utf-8') as f:
    for r,n,t,s in zip(ranking,names,teams,score):
        f.write(f'排名：{r}，名字：{n}，球队：{t}，得分：{s}\n')





