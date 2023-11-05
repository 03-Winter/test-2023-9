from PIL import Image
im=Image.open("D:\python\python实战案例\girls\img_f\刘亦菲阿布扎比旅拍高清壁纸.jpg")

w,h=im.size

image_row=4
image_column=4

import os
#保存jpg名字
names=os.listdir("D:\\python\python实战案例\girls\img_f")
#names=os.listdir("./girls/img_f")
#print(names)
#画出一块画布
new_image=Image.new('RGB',(image_column*w,image_row*h))
#循环输出每张jpg，然后粘粘到画布上
for y in range(image_row):
    for x in range(image_column):
        #打开图片
        o_img=Image.open("D:\\python\python实战案例\girls\img_f\\"+names[image_column*y+x])
        new_image.paste(o_img,(x*w,y*h))

#保存画布
new_image.save('new_img11111.jpg')











