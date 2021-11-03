from flask_cors import CORS
from flask import Flask, request, Response, jsonify
from PIL import Image
import os
import numpy as np
import cv2
import io
from io import BytesIO


port = int(os.getenv('PORT', 5000))
app = Flask(__name__)
CORS(app)

@app.route('/api/savefile', methods=['POST'])
def main():
    images = request.files.getlist("images")
    #images = ['15843']
    if images !=None:

        temp_ids=[]
        f_name=[]   #for file names
        for image_rec in images:
            img = image_rec.read()
            img = Image.open(io.BytesIO(img))
            npimg=np.array(img)
            image=npimg.copy()
            image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # OpenCV solo soporta BGR, tiene que ser pasado a RGB
            filename = image_rec.filename
            print("saving: ",filename)
            f_name.append(filename)
            wpath="./media/static/img/detections/"
            cv2.imwrite(wpath+filename,image)
    resp={}
    resp["status"]="SUCCESS"
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port, threaded=True)
