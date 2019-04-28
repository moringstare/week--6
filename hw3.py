# 请写一段代码
# 用蓝屏特效的原理
# 把stop.jpg的红色警示牌变成leaves.jpg中的树叶
from PIL import Image
img = Image.open("stop.jpg");
im1 = Image.open("leaves.jpg");
pixels = img.load()
pixel = im1.load()
x,y=img.size
for i in range(x):    
    for j in range(y):
        (r,g,b)=pixels[i,j]
        if r>(r+b+g)/3*1.5:
            pixels[i,j]=pixel[i,j]
img.show();
img.save("stop1.png", "PNG") 