# 现在有很多网站可以处理用户上传的图片，根据处理的复杂程度来收费
# 现在假设你负责开发这个网站的后台处理代码
# 张三负责把所有用户的需求和文件打包给你
# 网站开张后，张三收集到了一些需求和需要处理的图片
# 他把需求都写在了了 task.txt 中，图片都放在了文件夹中
# task.txt 的格式是固定的
# 一行一个任务, 每个任务的细节都用逗号分隔开, 以下举4个例子:
# 1. 变亮10%,cat5.jpg,cat5_o.png
#    意思: 把cat5.jpg文件整体变亮10%，存入cat5_o.png文件中
# 2. 蓝通图,cat0.jpg,cat0_o.png
#    意思: 把cat0.jpg文件变成蓝通图，存入cat0_o.png文件中
# 3. 部分灰度,1.2,curb.jpg,curb_o.png
#    意思: 把curb.jpg的局部变成灰度图, 选择部分的严格系数是1.2
# 4. 蓝屏特效,1.5,stop.jpg,leaves.jpg,sto_o.png 
#    意思: 把stop.jpg作为前景, leaves.jpg作为背景, 严格系数为1.5, 做蓝屏特效，把结果文件保存到sto_o.png
#
# 你的任务就是写一个程序，自动处理 task.txt 里面每一行的任务，并产生相应的结果文件
# 你可以用PO或者OO的思想来进行代码的编写
# 如果用PO的思想，要求函数要提取出来放在另一个文件tools.py中
# 如果用OO的思想，要求把类放在文件tools.py中
from tools import *
t = MyFile("task.txt")
q=t.getLines()
for i2 in q:
    for a in i2:
        newList1= a.split(",")
        List2= [newList1]
        for amount in List2:
            if len(amount)==3:
                for a,s,d in List2:
                    if a=='蓝通图':
                        b= BlueMap(s)
                        b.bluemap(d)
                    elif a=='绿通图':
                        b= GreenMap(s)
                        b.greenmap(d)
                    elif a=='红通图':
                        b=RedMap(s)
                        b.redmap(d)
                    elif a=="灰度图":
                        b=GreyMap(s)
                        b.greymap(d)
                    elif a=='变亮10%':
                        b=AddMap(s)
                        b.addmap(d)
                    elif a=='变暗10%':
                        b=AddMap(s)
                        b.addmap(d)
                        
            elif len(amount)==4:
                for a,s,d,f in List2:
                    if a=="部分灰度":
                        b=PartialGrayMap(d)
                        b.partialGrayMap(s,f)
            elif len(amount)==5:
                for a,s,d,f,g in List2:
                    if a=="蓝屏特效":
                        b=BlueScreenEffect(d,f)
                        b.blueScreenEffect(s,g)