#把 cat.png 变成红通图

from PIL import Image
img = Image.open("cat.png");
pixels = img.load()
x,y=img.size

for i in range(x):    # 扫描像素列表的每一行
    for j in range(y):    # 扫描某一行像素列表的每一列
        (r,g,b)=pixels[i,j]   # 获取第i行,第j列的像素的RGB
        pixels[i,j] = (r, 0, 0) # 只保留R值

img.save("cat_red.png", "PNG")    #把结果保存到cat_red.png文件中，指定保存的格式为png