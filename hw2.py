# 请模仿 image_4 写一段代码
# 实现生成curb.png中"路基部分"的灰度图
# 并把灰度图保存在curb_hui.png里
from PIL import Image
img = Image.open("curb.jpg");
pixels = img.load()
x,y=img.size

for i in range(x):    
    for j in range(y):    
        (r,g,b)=pixels[i,j] 
        if(r>50):
            avg=int((r+g+b)/3)
            pixels[i,j] = (avg,avg,avg)
img.show();
img.save("curb_hui.png", "PNG")    