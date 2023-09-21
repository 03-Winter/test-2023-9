# __all__=['sub']
# def sub(a,b):
#     print(a-b)
#
# def add(a,b):
#     print(a+b)
#
# if __name__ == '__main__':
#     sub(9,3)

# import primary1.test3
# print(primary1.test3.reverse("achieve"))
# print(primary1.test3.sub("achieve",0,6))
# print(primary1.test3.file_info("D:/t.txt"))
# print(primary1.test3.append_str("D:/test.txt","there is always hope behind you"))

# import json
# # 将列表转化为json
# data=[{"name":"jack","age":23},{"name":"mac","age":19}]
# json_str=json.dumps(data,ensure_ascii=False) #作用确保中文字符正常转化
# # 将字典转化为josn
# info={"name":"jack","age":23}
# json_str1=json.dumps(info,ensure_ascii=False) #作用确保中文字符正常转化
# print(json_str1)
# print(json_str)
# # 将json转化为python
# # json 就是字符串！！！！
# s='{"name":"jack","age":23}'
# d='[{"name":"jack","age":23},{"name":"mac","age":19}]'
# print(s)
# print(d)
# json.load(data)
#
# from pyecharts.options import *
# from pyecharts.charts import Line
#
# line=Line()
# line.add_xaxis(["China","Ammrica","Italy"])
# line.add_yaxis("GDP",[67,45,32])
# # 设置
# # 全局配置
# line.set_global_opts(
#     title_opts=(TitleOpts(title="测试",pos_left="center",pos_bottom="1%")),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True),
#     # tootip_opts=ToolboxOpts(is_show=True),
#
# )
#
# line.render()

import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts

f_us=open("D:/美国.txt",'r',encoding="UTF-8")
f_jp=open("D:/日本.txt",'r',encoding="UTF-8")
f_in=open("D:/印度.txt",'r',encoding="UTF-8")

us_data=f_us.read()
jp_data=f_jp.read()
in_data=f_in.read()

us_data=us_data.replace("jsonp_1629344292311_69436(","")
jp_data=jp_data.replace("jsonp_1629350871167_29498(","")
in_data=in_data.replace("jsonp_1629350745930_63180(","")

us_data=us_data[:-2]
jp_data=jp_data[:-2]
in_data=in_data[:-2]

# 将json转化为python字典
us_dict=json.loads(us_data)
jp_dict=json.loads(jp_data)
in_dict=json.loads(in_data)

us_trend_data=us_dict['data'][0]['trend']
jp_trend_data=jp_dict['data'][0]['trend']
in_trend_data=in_dict['data'][0]['trend']

us_x_data=us_trend_data["updateDate"][:314]
jp_x_data=jp_trend_data["updateDate"][:314]
in_x_data=in_trend_data["updateDate"][:314]

us_y_data=us_trend_data["list"][0]["data"][:314]
jp_y_data=jp_trend_data["list"][0]["data"][:314]
in_y_data=in_trend_data["list"][0]["data"][:314]

# 构建折线图
line=Line()
line.add_xaxis(us_x_data)

line.add_yaxis("美国确诊人数",us_y_data)
line.add_yaxis("日本确诊人数",jp_y_data)
line.add_yaxis("印度确诊人数",in_y_data)
line.set_global_opts(

title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%")
)

line.render("美日印.html")

f_us.close()
f_jp.close()
f_in.close()























