# 第6周的作业: Python 批量处理图片

#### 要求
1. 完成`hw1.py`: 实现`灰度图`
2. 完成`hw2.py`: 实现局部`灰度图`
3. 完成`hw3.py`: 实现`蓝屏特效`
4. 完成`hw4.py`: 实现图片批量处理


#### 必备知识: 用Pillow处理图形

首先请确定你的`Pillow`库已经被安装
![输入图片说明](https://gitee.com/uploads/images/2019/0407/160117_acd61817_4797169.png "下载pillow包.png")

注意: 所有代码都已经提供，可以尽情的尝试。
#### 1. 读取 并 显示 图像: `image_1.py`
```
from PIL import Image   #引入PIL包中的Image类

# 通过Image类的open方法读取图片 cat.png的内容，保存在img对象中
img = Image.open("cat.png");   

img.show();   #通过调用img对象的show()方法显示图片
```
注意，`Image`类没有使用一般的实例化过程，而使用了类方法`open`产生了一个对象。是因为图片的处理需要一种技术叫做`lazy initialization`即`懒惰初始化`，感兴趣的同学可参看网页[https://zh.wikipedia.org/wiki/惰性初始模式]中的`python`部分代码。

#### 2. 把图像放大10倍: `image_2.py`
```
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

img.save("x_10.png", "PNG")    #把结果保存到x_10.png文件中，指定保存的格式为png
```
注意: 元组是什么? 其实很简单，元组(1,2)其实就是列表[1,2]。只是元组有一个特性: 不能修改。别的就和列表没差别了。

#### 3. 把图像的左上角变成红色的: `image_3.py`
```
#把 x.png 的左上角变成红色的

from PIL import Image
img = Image.open("x.png");

#把像素(0,0)变成红色的
pixels = img.load()         #读取图片的像素坐标系，放入 pixels
pixels[0,0] = (255,0,0)     #把像素矩阵第(0,0)点的RGB设置成(255,0,0)

#放大30倍, image_2中已经讲解
x,y=img.size
img=img.resize((x*30, y*30))

img.save("x_red.png", "PNG")    #把结果保存到x_red.png文件中，指定保存的格式为png
```
注意, `load`方法会把整个x.png图片![输入图片说明](https://gitee.com/uploads/images/2019/0407/161948_635306d7_4797169.png "x_10.png")的像素坐标系返回

每一个坐标系中都存有一个RGB值的元组，如图所示:
![输入图片说明](https://gitee.com/uploads/images/2019/0407/161446_2fb6455e_4797169.png "xpng像素坐标系.png")

所以，代码`pixels[0,0] = (255,0,0)`就成功的把`(0,0)`处的RGB变成了`(255,0,0)`也就是`红色`
![输入图片说明](https://gitee.com/uploads/images/2019/0407/161811_42c81600_4797169.png "xpng像素坐标系左上角红色.png")

#### 4. 把图像变成红通图: `image_4.py`
```
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
```
如果你对for循环的嵌套不是太理解，可以看看下面这个例子:
```
l=[[1,2], [3,4]]
for i in range(2):
    print(l[i])
```
这段代码会打印:
```
[1,2]
[3,4]
```
原因很简单:
- 当`i=0`的时候`l[0]`即`l`的第一个元素是: `[1,2]`
- 当`i=1`的时候`l[1]`即`l`的第二个元素是: `[3,4]`

所以，如果想要单独访问1,2,3,4, 就需要在此基础上再加一个循环:
```
l=[[1,2], [3,4]]
for i in range(2):
    for j in range(2):
        print(l[i][j])
```
当`i=0`时，j从0开始计数，所以:
- 第1次`i=0`, `j=0`, 打印: `l[0][0]`是1
- 第2次`i=0`, `j=1`, 打印: `l[0][1]`是2
- 第3次`i=1`, `j=0`, 打印: `l[1][0]`是3
- 第4次`i=1`, `j=1`, 打印: `l[1][1]`是4