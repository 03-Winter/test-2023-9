#学习python的第一天
"""
money = 98
print("heloo world!!")
print(222)
print("多少钱：",money)
"""



#学习python的第二天

# a=type(222)
# print(type(333))
# print(a)
# num=2
# num **=2
# print("numdezhiwei :",num)
# name_1='\"hello\"'
# name_2="\'world"
# print(name_1)
# print(name_2)
# name="hello"
# adress="world"
# print("nohao:"+name+",shijie:"+adress)
# name="zhong"
# number=34
# float=3.1415926
# messa="wodemingzishi:%7s" % name
# messag="wodemingzishi:%2d" % number
# message="wodemingzishi:%1.5f" % float
# print(messa)
# print(messag)
# print(message)
#name="chuanzhiboke"
# stock_price=19.99
# stock_code="003032"
# stock_price_daily_growth_factor=1.2
# growth_day=7
# print("每日增长系数是：%.1f,经过七天的增长后，股价达到了：%d" % (stock_price_daily_growth_factor,stock_price))
# print(f"公司：{name},股票代码：{stock_code}，当前股价：{stock_price* stock_price_daily_growth_factor**growth_day}")
# num1=23
# num2=43
# print(num1==num2)

# guess_num=int(input("请输入数字"))
# if guess_num==num:
#     print("daduil")
# else:
#     if guess_num == num:
#         print("gaiduil")
#     else:
#         print("caixiaol")
#         guess_num=int(input("qingchongxinshuru"))
#         if guess_num==num :
#             print("caiduil")
#         else:
#             if guess_num>num:
#               print("caidal")
#             else:
#               print("caixiaol")
# age=int(input("请输入你的年龄："))
# if age>=18 :
#     print(f"你已成年，游玩需要补票30")
# else:
#     print(f"免票")
# sum=0
# i=1
# while i<=100 :
#     sum +=i
#     i +=1
# print(sum)
#
# import random
# num=random.randint(1,10)
# count=0
# flag=1
# while flag :
#     guess_num=int(input("请输入数字"))
#     if guess_num==num :
#         print("答对了")
#         flag=False
#     else:
#         if guess_num>num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print("恭喜你赢了")
#
#九九乘法表
# i=1
# while i<=9 :
#     j=1
#     while j<=i :
#         print(f"{i}*{j}={i*j}\t",end='')
#         j +=1
#     i += 1
#     print()
# num=12
# y=4
# x=34
# input(num)
# for y in range(num):
#     print(y)
# for y in range(num,x):
#     print(y)
# for y in range(num,x,2):
#     print(y)
# import random
# sum=10000
# worker=0
# while worker<=20 :
#     worker +=1
#     num = random.randint(1, 10)
#     if num<5 :
#         print("业绩不够")
#         continue
#     else:
#         sum -=1000
#         print(f'worker{worker}拿到了工资')
#         if sum<=00 :
#             print("余额不足")
#             break
#
# for i in range(1,21) :
#     num = random.randint(1, 10)
#     if num<5 :
#         print("业绩不够")
#         continue
#     else:
#         sum -=1000
#         print(f'worker{i}拿到了工资')
#         if sum<=0 :
#             print("余额不足")
#             break

# def check(num):
#     if num>=37.5 :
#         print("发烧了")
#     else:
#         print("meiyou")
#
# num=0
# num=int(input())
# check(num)
# my_list=['hello','error','hinder']
# print(my_list[1])
# print(my_list[-1])
# my_liste=[[1,2,3],[3,4,5]]
# print(my_liste[1][1])

#list=[1,2,3,4,5,6,7,2,2,3,45,5]
# a=list.index(3)
#a=list.index(32)
# list[3]=2
# a=list.index(2)
#a=list.insert(3,0)前面为下标，后面为元素
# a=list.append(33)
# a=list.extend([3,4,5,6,8])
# del list[3]
# a=list[3]
#a=list.pop(3)
#print(list[3])
#a=list.remove(2)
#list.clear()
#a=list.count(2)
# a=len(list)
# print(a)

# import cv2 #opencv读取的格式是BGR
# import matplotlib.pyplot as plt
# import numpy as np
# #%matplotlib inline
# img=cv2.imread('ch.jpg')
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#学python的第三天

# my_str="日落的夕阳"
# #value=my_str.replace("日落","今晚")
# value=my_str.split("的")
# print(f"{my_str},{value}")
# my_str="itheitma itcast boxuegu"
# value=my_str.count("it")
# key=my_str.replace(" ","|")
# print(f"{key}")
# im=my_str.split(" ")
# print(f"{im}")
# print(f"{value}")
# my_str="物来外天，仙飞外天lia，净二干一"
# o = my_str.split(", ")[0].replace("lia","")[::-1]
# print(f"{o}")











