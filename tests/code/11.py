from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from imutils import paths
from sklearn import preprocessing
import numpy as np
import argparse
import imutils
import cv2
import os
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pickle  
 

def vistDir(path,filelist):
    
    zifile=os.listdir(path)
    for i in zifile:
        pathname=os.path.join(path,i)
        if not os.path.isfile(pathname):
            vistDir(pathname,filelist)
        else:
            filelist.append(pathname)
    return filelist
def image_to_feature_vector(image):
	# resize the image to a fixed size, then flatten the image into
	# a list of raw pixel intensities
    
	return image.flatten()
'''
def extract_color_histogram(image, bins=(32, 32, 32)):
	# extract a 3D color histogram from the HSV color space using
	# the supplied number of `bins` per channel
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	hist = cv2.calcHist([hsv], [0, 1, 2], None, bins,
		[0, 180, 0, 256, 0, 256])

	# handle normalizing the histogram if we are using OpenCV 2.4.X
	if imutils.is_cv2():
		hist = cv2.normalize(hist)

	# otherwise, perform "in place" normalization in OpenCV 3
	else:
		cv2.normalize(hist, hist)

	# return the flattened histogram as the feature vector
	return hist.flatten()
'''


# construct the argument parse and parse the arguments
'''
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1,
	help="# of nearest neighbors for classification")
args = vars(ap.parse_args())
'''
# define example
data = ['axes', 'carabiners', 'gloves', 'harnesses', 'insulated_jackets', 'rope', 'boots', 'crampons', 'hardshell_jackets', 'helmets','pulleys','tents']

# grab the list of images that we'll be describing
print("[INFO] handling images...")
filelist=[]
imagePaths = vistDir("/home/zhangyf/notebooks/zhangyf/gear_images_trans",filelist)

# initialize the raw pixel intensities matrix, the features matrix,
# and labels list
rawImages = []
features = []
labels = []

# loop over the input images
for (i, imagePath) in enumerate(imagePaths):
	# load the image and extract the class label
	# our images were named as labels.image_number.format
	image = cv2.imread(imagePath)
    # get the labels from the name of the images by extract the string before "."
	label = imagePath.split(".")[-1]

	# extract raw pixel intensity "features"
    #followed by a color histogram to characterize the color distribution of the pixels
	# in the image
	pixels = image_to_feature_vector(image)
	#hist = extract_color_histogram(image)

	# add the messages we got to the raw images, features, and labels matricies
	rawImages.append(pixels)
	#features.append(hist)
	labels.append(label)

	# show an update every 200 images until the last image
	if i > 0 and ((i + 1)% 200 == 0 or i ==len(imagePaths)-1):
		print("[INFO] processed {}/{}".format(i+1, len(imagePaths)))
min_max_scaler = preprocessing.MinMaxScaler()


# show some information on the memory consumed by the raw images
# matrix and features matrix
rawImages = np.array(rawImages)
#rawImages= min_max_scaler.fit_transform(rawImages)
#features = np.array(features)
#labels = np.array(labels)
values = np.array(labels)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
#integer_encoded = min_max_scaler.fit_transform(integer_encoded)
print(integer_encoded)
# binary encode
#onehot_encoder = OneHotEncoder(sparse=False)
#integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
#onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
#print(onehot_encoded)

print(rawImages)
print(labels)
print("[INFO] pixels matrix: {:.2f}MB".format(
	rawImages.nbytes / (1024 * 1000.0)))
#print("[INFO] features matrix: {:.2f}MB".format(
#	features.nbytes / (1024 * 1000.0)))

# partition the data into training and testing splits, using 85%
# of the data for training and the remaining 15% for testing
(trainRI, testRI, trainRL, testRL) = train_test_split(
	rawImages, integer_encoded, test_size=0.1, random_state=42)
#(trainFeat, testFeat, trainLabels, testLabels) = train_test_split(
#	features, labels, test_size=0.15, random_state=42)



#SVC
print("\n")
print("[INFO] evaluating raw pixel accuracy...")
model = SVC(max_iter=1000,C=1,kernel='linear')
model.fit(trainRI, trainRL)
acc = model.score(testRI, testRL)
# 保存模型
with open('model.pickle', 'wb') as f:
    pickle.dump(model, f) 
print("[INFO] SVM-SVC raw pixel accuracy: {:.2f}%".format(acc * 100))