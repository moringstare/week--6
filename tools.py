class MyFile():
    def __init__(self, file):
        self.file=file
    def getAll(self):
        with open(self.file,'r') as f:
            return f.read();
    def getLines(self):
        with open(self.file,'r') as f:
            return [x.split(' ') for x in f.read().split("\n")]
class BlueMap():
    def __init__(self,img):
        self.img=img
        
    def bluemap(self, ok):
        from PIL import Image
        i=Image.open(self.img);
        pixels=i.load()
        (x,y)=i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                pixels[n,m]=(0,0,b)
            i.save(ok,"PNG")
class GreenMap():
    def __init__(self, img):
        self.img=img
        
    def greenmap(self,ok):
        from PIL import Image 
        i=Image.open(self.img);
        pixels=i.load()
        (x,y)=i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                pixels[n,m]=(0,g,0)
            i.save(ok,"PNG")
class RedMap():
    def __init__(self,img):
        self.img=img
        
    def redmap(self, ok):
        from PIL import Image 
        i=Image.open(self.img);
        pixels=i.load()
        (x,y)=i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                pixels[n,m]=(r,0,0)
            i.save(ok,"PNG")
class GreyMap():
    def __init__(self,img):
        self.img=img

    def greymap(self,ok):
        from PIL import Image 
        i=Image.open(self.img);
        pixels=i.load()
        (x,y)=i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                avg=int((r+g+b)/3)
                pixels[n,m]=(avg,avg,avg)
        i.save(ok,"PNG")
class AddMap():
    def __init__(self,img):
        self.img=img
        
    def addmap(self,ok):
        from PIL import Image 
        i=Image.open(self.img);
        pixels=i.load()
        (x,y)=i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                add=int((r+g+b)*1.1)
                pixels[n,m]=(add,add,add)
                
class LessMap():
    def __init__(self, img):
        self.img=img
        
    def lessmap(self,ok):
        from PIL import Image
        i=Image.open(self.img);
        pixels=i.load()
        (x,y)=i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                less=int((r+g+b)*0.9)
                pixels[n,m]=(less,less,less)
        i.save(ok, "PNG")
class PartialGrayMap():
    def __init__(self,img):
        #self huidu=huidu
        self. img=img
        
    def partialGrayMap(self,huidu,ok):
        from PIL import Image
        i = Image.open(self.img);
        pixels = i.load()
        (x,y) = i.size
        for n in range(x):
            for m in range(y):
                (r,g,b)=pixels[n,m]
                avg=int((r+g+b)/3)
                if r>100*float(huidu):
                    pixels[n,m]=(avg,avg,avg)
        i.save(ok,"PNG")
class BlueScreenEffect():
    def __init__(self,img,back):
        self. img=img
        self.back=back
    def blueScreenEffect(self, huidu,ok):
        from PIL import Image
        i= Image. open( self.img);
        B= Image. open(self. back)
        pixels1=i.load()
        pixelsB=B.load()
        (x,y)=i.size
        for m in range(x):
            for n in range(y):
                (r,g,b)=pixels1[m,n]
                avg=int((r+g+b)/3)
                if r>avg*float(huidu):
                    (rb, gb, bb)=pixelsB[m,n]
                    pixels1[m,n]=(rb,gb,bb)
        i.save(ok,"PNG")