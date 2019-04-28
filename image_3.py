#把 x.png 的左上角变成红色的

from PIL import Image
img = Image.open("x.png");

#把像素(0,0)变成红色的
pixels = img.load()         #读取图片的像素坐标系，放入 pixels
pixels[0,0] = (255,0,0)     #把像素矩阵第(0,0)点的RGB设置成(255,0,0)

#放大30倍, image_2中已经讲解
x,y=img.size
img=img.resize((x*30, y*30))
img.show();
img.save("x_red.png", "PNG")    #把结果保存到x_red.png文件中，指定保存的格式为png
