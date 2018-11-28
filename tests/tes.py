from sklearn import tree
import skimage.io as io
from skimage import data_dir
import numpy as np
from sklearn.svm import SVC


#批量读取图片文件，及对应标签
def createDataSet():
    imgList = []
    # labelList = ['axes', 'boots', 'carabiners', 'crampons', 'gloves', 'hardshell_jackets', 'harnesses', 'helmets', 'insulated_jackets', 'pulleys', 'rope', 'tents']
    labelList = ['gloves', 'helmets']
    k = 0
    while k<3:
        for i in labelList:
            str='/Users/yml/Desktop/gear_images_a/' + i + '/*.*'
            coll = io.ImageCollection(str) # 文档存在 coll 中
            print(coll[0:2])
            imgList.append(coll)
        k += 1
    print(imgList[0][0][0].shape) # (180, 3)
    print(type(imgList[0][0][0])) #numpy.ndarray
    print(type(imgList[0][0]))   #numpy.ndarray
    print(len(imgList[0]))    # 215
    print(type(imgList[0]))   #io.collection
    # io.imshow(imgList[0][0])  #查看图片
    # io.show()
    return imgList, labelList

def SVM(X,y,XX):
    
    model = SVC(C=1.0)
    model.fit(X,y)

    predicted = model.predict(XX)
    return predicted

## 输入图片
inpic = []; inpic1 = []; inpic2 = []; 
imgList, labelList = createDataSet()
for i in imgList[0]:
    mm = i.flatten()
    inpic1.append(np.array(mm))
inpic.append(inpic1)
for i in imgList[1]:
    mm = i.flatten()
    inpic2.append(np.array(mm))
inpic.append(inpic2)
inpic = np.array(inpic)
print('inpic',len(inpic))

## 测试图片
pred_pic = []
str_predict='/Users/yml/Desktop/test_pic.jpeg'
coll_predict = io.ImageCollection(str_predict) 
coll_predict = (np.array(coll_predict)).flatten()
coll_predict = np.array(coll_predict)
pred_pic.append(coll_predict)
pred_pic = np.array(pred_pic)
print('pred_pic', len(pred_pic))

## labels
label = []
label.append(np.zeros(215))
label.append(np.ones(95))
label = np.array(label)
print(inpic)

## 测试
out = SVM(inpic.reshape(1,-1), label, coll_predict)
print(out)
