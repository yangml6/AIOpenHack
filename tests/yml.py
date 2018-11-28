from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

desired_size = 128
im_pth = "/Users/yml/Desktop/125475.jpeg"

im = Image.open(im_pth)
old_size = im.size  # old_size[0] is in (width, height) format

ratio = float(desired_size)/max(old_size)
new_size = tuple([int(x*ratio) for x in old_size])

im = im.resize(new_size, Image.ANTIALIAS)
print(old_size)

# new_im = Image.new("RGB", (desired_size, desired_size),(255,255,255))
new_im = Image.new("RGB", (desired_size, desired_size),(255,255,255))

#方式一
new_im.paste(im, ((desired_size-new_size[0])//2,
                    (desired_size-new_size[1])//2))

# new_im.show()

imgplot = plt.imshow(new_im) #只能用这个形式展示图片
plt.show(imgplot)

#方式二
delta_w = desired_size - new_size[0]
delta_h = desired_size - new_size[1]
padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
new_im = ImageOps.expand(im, padding,(255,255,255))

imgplot = plt.imshow(new_im)
plt.show(imgplot)

# plt.show(new_im)
print(new_im.size)



#### from PIL import Image
from numpy import *
from pylab import *

def histeq(im,nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""

    #计算图像的直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed = True)
    cdf = imhist.cumsum() #累计分布函数
    cdf = 255 * cdf / cdf[-1] #归一化

    #使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf

#gray()
# im = array(Image.open("112127.jpeg").convert("RGBA"))
# im = array(Image.open("112127.jpeg"))
im = array(new_im)
im2,cdf = histeq(im)

subplot(1,2,1)
imshow(im)
title("Original picture")
axis('off')

subplot(1,2,2)
imshow(im2)
title("Equilibrium picture")
axis('off')

show()




from skimage import data,exposure
import matplotlib.pyplot as plt
img=array(new_im)
plt.figure("hist",figsize=(8,8))

arr=img.flatten()
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始图像
plt.subplot(222)
plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='blue') #原始图像直方图

img1=exposure.equalize_hist(img)
arr1=img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均RGBA
plt.subplot(224)
plt.hist(arr1, bins=256, normed=1,edgecolor='None',facecolor='blue') #均衡化直方图

plt.show()