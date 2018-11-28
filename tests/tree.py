from sklearn import tree
import skimage.io as io
from skimage import data_dir
import numpy as np
from sklearn.svm import SVC


#批量读取图片文件，及对应标签
def createDataSet():
    imgList = []
    # labelList = ['axes', 'boots', 'carabiners', 'crampons', 'gloves', 'hardshell_jackets', 'harnesses', 'helmets', 'insulated_jackets', 'pulleys', 'rope', 'tents']
    labelList = ['axes',  'gloves', 'helmets']

    for i in labelList:
        str='/Users/yml/Desktop/gear_images/gear_images/' + i + '/*.*'
        coll = io.ImageCollection(str) # 文档存在 coll 中
        imgList.append(coll)

    print(imgList[0][0][0])
    io.imshow(imgList[0][0])  #查看图片
    io.show()
    return imgList, labelList

def SVM(X,y,XX):
    
    model = SVC(C=5.0)
    model.fit(X,y)

    predicted = model.predict(XX)
    return predicted

str_predict='/Users/yml/Desktop/test_pic.jpeg'
coll_predict = io.ImageCollection(str_predict) 

imgList, labelList = createDataSet()
out = SVM(imgList, labelList, coll_predict)
print(out)