from file_define import JsonFileReader,FileReader,TextFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_define=TextFileReader("D:/2011年1月销售数据.txt")
json_file_define=JsonFileReader("D:/2011年2月销售数据JSON.txt")

text_file_reader:list[Record]=text_file_define.read_data()
json_file_reader:list[Record]=json_file_define.read_data()

all_data:list[Record]=text_file_reader+json_file_reader

data_list={}
for record in all_data:
    if record.date in data_list.keys():
        data_list[record.date] += int(record.money)
    else:
        data_list[record.date] = int(record.money)

bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_list.keys()))
bar.add_yaxis("销售额",list(data_list.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("一二月销售额.html")






























