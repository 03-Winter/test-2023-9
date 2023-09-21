# class students:
#     name=None
#     age=None
#
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __le__(self,other):
#         return self.age<other.age
#
#     def __lt__(self, other):
#         return self.age<=other.age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     def Hi(self):
#         print(f"niaho{self.name}")
#
# stu=students("jack",18)
# stu1=students("jac",18)
#
# print(stu<stu1)
# stu.name="jack"
# stu.Hi()
from random import random

# 私有成员仅提供内部使用
# class Phone:
#     # __current_voltage=5
#     __is_5g_enable=True
#     def __keep_single_core(self):
#         print("以单核模式运行")
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭")
#     def call_by_5g(self):
#         self.__check_5g()
#         if self.__is_5g_enable:
#             print("yes")
#         else:
#             print("no")
#
# phone=Phone()
# phone.call_by_5g()

# class Phone:
#     id=234
#     def fun(self):
#         print("as")
# class Phone2022(Phone):
#     name=None
#     def func(self):
#         print("we")
#
# class NFC:
#     def read(self):
#         print("card")
# class remote:
#     def red(self):
#         print("machine")
# class MyPhone(Phone,NFC,remote):
#     pass
# phone=MyPhone()
# phone.name="jack"
# print(phone.id)
# print(phone.name)
# print(phone.read())
# print(phone.red())
# from typing import Union
#
# def func(data:Union[int,str]):
#     pass

# class AC:
#     def cool_wind(self):
#         pass
#     def hot_wind(self):
#         pass
#     def swing_l_r(self):
#         pass
# class  Midea(AC):
#     def cool_wind(self):
#         print("美的冷风")
#     def hot_wind(self):
#         print("美的热风")
#     def swing_l_r(self):
#         print("美的摆动")
#
# class Gree(AC):
#     def cool_wind(self):
#         print("格力冷风")
#     def hot_wind(self):
#         print("格力热风")
#     def swing_l_r(self):
#         print("格力摆动")
#
# def make_cool(ac):
#     ac.cool_wind()
#
# midea_ac=Midea()
# gree_ac=Gree()
#
# make_cool(midea_ac)
# make_cool(gree_ac)










