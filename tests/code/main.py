from flask import Flask
from flask import request
from flask import jsonify
import numpy as np
import platform
from sklearn.externals import joblib
from PIL import Image

app = Flask(__name__)

model = None

def init():
    global model
    model = joblib.load("svm.pkl")

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
        im = Image.open(imgPath)
        imp = np.asarray(im, dtype=np.uint8).flatten()
        imp = imp.reshape((1, 97200))
        result = model.predict(imp)
        restr = "result: %d" % result[0]
        return restr

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
