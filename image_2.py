#把 x.png 放大10倍
from PIL import Image
img = Image.open("x.png");

(x,y)=img.size    #img.size会返回一个长和宽(单位是像素)的元组, 这里把长存到x, 宽存到y里
new_x=x*10
new_y=y*10

#把长和宽都乘以十倍之后，以元组的形式放入img的resize方法里
#resize的意思就是重新定义大小，该方法会返回一个新的变过大小之后的对象
#再次把新的对象存到img中，就OK了
img=img.resize((new_x, new_y))
#之所以有两个小括号，只是因为[new_x, new_y]写成了元组的形式(new_x, new_y)
#所以看起来好像用了两个小括号,实际上是外面的括号里面放了一个元组(new_x, new_y)
img.show();
img.save("x_10.png", "PNG")    #把结果保存到x_10.png文件中，指定保存的格式为png

