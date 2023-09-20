from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f=open("D:/1960-2019全球GDP数据.csv",'r',encoding="GB2312")
data_line=f.readlines()
f.close()

data_line.pop(0)
data_dict={}
for line in data_line:
    year=line.split(",")[0]
    contry=line.split(",")[1]
    gdp=float(line.split(",")[2])
    try:
        data_dict[year].append([contry,gdp])
    except Exception as e:
        data_dict[year]=[]
        data_dict[year].append([contry, gdp])
timeline=Timeline({"Theme":ThemeType.LIGHT})
sorted_year_dict=sorted(data_dict.keys())
for year in sorted_year_dict:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for contry_gdp in year_data:
        x_data.append(contry_gdp[0])
        y_data.append(contry_gdp[1]/100000000)


    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.add_xaxis(x_data)
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP数据")
    )
    timeline.add(bar, str(year))
timeline.add_schema(
    is_loop_play=False,
    is_auto_play=True,
    is_timeline_show=True,
    play_interval=1000
)

timeline.render("全球GDP前八数据.html")






















