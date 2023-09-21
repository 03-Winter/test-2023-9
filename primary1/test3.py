# import time

#f=open("D:/test.txt","r",encoding="UTF-8")
# print(f"{f.read(23)}")
# print(f"{f.read()}")
# line=f.readlines()
# for line in line:
#     print(line)
#time.sleep(3000)
# f.close()
# with open("D:/test.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(line)
#
# word=f.read()
# word=word.strip()
# count=word.count("家长")
# print(count)
# f=open("D:/text.txt","w",encoding="UTF-8")
# f.write("好好学习")
# # f.flush()
# # f.write("\nsee you again")
# f=open("D:/text.txt","a",encoding="UTF-8")
# f.write("\nis correct")

# line=f.remove('(')
# line=f.remove(")"," ")
# line=f.remove(","," ")
# fr=open("D:/test.txt","r",encoding="UTF-8")
# fw=open("D:/test.txt.bak","w",encoding="UTF-8")
# for line in fr:
#     line=line.strip()
#     # print(type(line))
#     # line=line.split(",")
#     # print(line.split(",")[-1])
#     if line.split(",")[-2]=="男":
#         print(line)
#         # continue
#     fw.write(line)
#     fw.write('\n')
# fw.close()
# fr.close()

# try:
#     # 1/0
#     print(name)
# except (NameError,ZeroDivisionError) as e:
#     print(e)

# try:
#     f=open("D:/abc.tet",'r',encoding="UTF-8")
# except Exception as e:
#     print("error")
#     f=open("D:/abc.tet",'w',encoding="UTF-8")
# else:
#     print("successfully")
# finally:
#     f.close()
# def fun1():
#     print("1")
#     num=1/0
#     print('2')
# def fun2():
#     print('3')
#     fun1()
#     print("4")
# def main():
#     fun2()
# main()
# from time import sleep as sl
# print("hello")
# sl(5)
# print("world]")

# print("affasa")
# from test4 import*
# sub(8,3)

def reverse(s):
    return s[::-1]


def sub(s,x,y):
    return s[x:y]

def file_info(s):
    f = None
    try:
        f=open("D:/test.txt",'r',encoding="UTF-8")
        content=f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

def append_str(s,data):
    v=open(s,'a',encoding="UTF=8")
    v.write(data)
    v.write("\n")
    v.close()

