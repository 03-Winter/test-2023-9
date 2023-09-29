# def outer(logo):
#     def inner(msg):
#         print(f'{logo},{msg},{logo}')
#     return inner
#
# fn=outer("hello")
# fn("world!!")

# def account_create(initial_account=0):
#     def atm(num,deposite=True):
#         nonlocal initial_account
#         if deposite:
#             initial_account+=num
#             print(f'存款，账户余额：{initial_account}')
#         else:
#             initial_account -=num
#             print(f'取款，账户余额：{initial_account}')
#     return atm
#
# fn=account_create()
# fn(12)
# fn(400)
# fn(200,False)

# def outer(func):
#     def inner():
#         print(f'sleep')
#         func()
#         print(f'wake')
#     return inner
#
# def sleep():
#     import time
#     import random
#     print(f'sleeping')
#     time.sleep(random.randint(1,4))
#
# fn=outer(sleep)
# fn()

# def outer(func):
#     def inner():
#         print(f'sleep')
#         func()
#         print(f'wake')
#     return inner
# @outer
# def sleep():
#     import time
#     import random
#     print(f'sleeping')
#     time.sleep(random.randint(1,4))
#
# sleep()


# class Person:
#     pass
# class Work(Person):
#     pass
# class Student(Person):
#     pass
# class Teacher(Person):
#     pass
# class Factory(Person):
#     def get_person(self,p_type):
#         if p_type=='w':
#             return Work()
#         elif p_type=='s':
#             return Student()
#         else:
#             return Teacher()
#
# fac=Factory()
# work=fac.get_person('w')
# student=fac.get_person('s')
# teacher=fac.get_person('t')

# 多线程的使用

# import time
# import threading
#
# def sing(msg):
#     while True:
#         print(msg)
#         time.sleep(1)
# def dance(msg):
#     while True:
#         print(msg)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     sing_thread=threading.Thread(target=sing,args=("singing",))
#     dance_thread=threading.Thread(target=dance,kwargs={"msg":"dancing"})
#
#     sing_thread.start()
#     dance_thread.start()




