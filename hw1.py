# 请模仿 image_4 写一段代码
# 实现生成cat.png的灰度图
# 并把灰度图保存在cat_hui.png里
from PIL import Image
img = Image.open("cat.png");
pixels = img.load()
x,y=img.size

for i in range(x):    
    for j in range(y):   
        (r,g,b)=pixels[i,j] 
        avg =int ((r+g+b)/3)
        pixels[i,j] = (avg,avg,avg) 
img.show();
img.save("cat_hui.png", "PNG")    