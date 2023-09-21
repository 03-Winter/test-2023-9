# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
# map=Map()
#
# data=[
#     ("北京",123),
#     ("上海",234),
#     ("湖南",345),
#     ("台湾",456),
#     ("广东",567)
# ]
#
# map.add("测试",data,"china")
#
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=False,
#         pieces=[
#             {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
#             {"min":10,"max":99,"label":"10-99","color":"#FFFF99"},
#             {"min":100,"max":119,"label":"100-119","color":"#FF9966"},
#             {"min":120,"max":149,"label":"120-149","color":"#FF6666"},
#             {"min":150,"max":9999,"label":"150-9999","color":"#990033F"},
#         ]
#     )
# )
#
# map.render("地图.html")

import json
from pyecharts.charts import Map
from pyecharts.options import *

# f=open("D:/疫情.txt",'r',encoding="UTF-8")
# data=f.read()
# f.close()
#
# data_dict=json.loads(data)
#
# province_data_dict=data_dict["areaTree"][0]["children"]
# data_list=[]
# for province_data in province_data_dict:
#     province_name=province_data["name"]+"省"
#     province_confirm=province_data["total"]["confirm"]
#     data_list.append((province_name,province_confirm))
#
# # print(data_list)
# map=Map()
# map.add("各省份确诊人数",data_list,"china")
#
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"10-99","color":"#FFFF99"},
#             {"min":1000,"max":9999,"label":"100-119","color":"#FF9966"},
#             {"min":10000,"max":99999,"label":"120-149","color":"#FF6666"},
#             {"min":100000,"label":"150-9999","color":"#990033"},
#         ]
#     )
# )
#
#
# map.render("全国疫情图.html")

# f=open("D:/疫情.txt",'r',encoding="UTF-8")
# data=f.read()
# f.close()
#
# data_dict=json.loads(data)
#
# province_data=data_dict["areaTree"][0]["children"][3]["children"]
#
# data_list=[]
#
# for city_data in province_data:
#     city_name=city_data["name"]+"市"
#     city_confirm=city_data["total"]["confirm"]
#     data_list.append((city_name,city_confirm))
# print(data_list)
# map=Map()
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"10-99","color":"#FFFF99"},
#             {"min":1000,"max":9999,"label":"100-119","color":"#FF9966"},
#             {"min":10000,"max":99999,"label":"120-149","color":"#FF6666"},
#             {"min":100000,"label":"150-9999","color":"#990033"},
#         ]
#     )
# )
# map.add("省",data_list,"河南")
#
# map.render("河南省确诊人数.html")


from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
bar =Bar()

bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[23,34,45],label_opts=LabelOpts(position="right"))
bar.reversal_axis()
bar1=Bar()

bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[33,44,55],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar2 =Bar()

bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[54,43,32],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
# bar.render("基础柱状图.html")

timeline=Timeline(
    {"theme":ThemeType.LIGHT}
)
timeline.add(bar,"one")
timeline.add(bar1,"two")
timeline.add(bar2,"three")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True

)
timeline.render("时间线柱状图.html")







