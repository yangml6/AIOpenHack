from flask import Flask
from flask import request
from flask import jsonify
import numpy as np
import platform
from PIL import Image
from sklearn.externals import joblib

app = Flask(__name__)

model = None

def init():
    global model
    model = joblib.load('svm.model')

@app.route('/')
def hello_world():
    a = platform.python_version()
    return a

@app.route('/upload', methods=['POST'])
def upload_file():
    if model ==None:
        init()
    if request.method == 'POST':
        f = request.files['the_file']
        imgPath = 'a.jpg'
        f.save(imgPath)
        im = Image.open(im_pth)
        imarray = np.asarray(im, dtype=np.uint8)
        n_imarray = imarray.flatten()
        x = np.array(n_imarray)
        preds = model.predict(x)
        return 'predicted:',preds

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)