from PIL import Image   #引入PIL包中的Image类

# 通过Image类的open方法读取图片 cat.png的内容，保存在img对象中
img = Image.open("cat.png");   

img.show();   #通过调用img对象的show()方法显示图片
