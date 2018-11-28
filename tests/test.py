from PIL import Image, ImageOps
import os
import numpy as np

def travel(orgpth, outpth):
    fs = os.listdir(orgpth)  
    for f in fs:
        tmp_path = os.path.join(orgpth, f)
        if not os.path.isdir(tmp_path):  
            print('do with file: %s'%tmp_path)
            img_0,label_0 = processfile(tmp_path)
            img.append(img_0)
            if label_0 not in label:
                label.append(label_0)
        else:
            print('do with dir: %s'%tmp_path)
            outpth2 = os.path.join(outpth, f)
            os.mkdir(outpth2)
            travel(tmp_path, outpth2)

def processfile(im_pth):
    im = Image.open(im_pth)
    imarray = np.asarray(im, dtype=np.uint8)
    n_imarray = imarray.flatten()
    label = im_pth.split('/')[-2]
#     pca = PCA(n_components=2)  
#     n_imarray = pca.fit_transform(imarray)
#     PCA(copy=True, n_components=2, whiten=False) 
#     print(n_imarray,n_imarray.shape)
#     print(im_pth.split('/')[-2])
    return n_imarray,label