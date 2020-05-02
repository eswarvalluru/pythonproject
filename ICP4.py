from werkzeug.utils import secure_filename
import joblib
from flask import Flask, request, render_template
import cv2
import numpy as np

# Define a flask app
app = Flask(__name__)
def process_eval(imk):
    output1 = cv2.resize(imk, (28,28))
    output1 = output1.astype('float')
    output1 /= 255.0
    print(type(output1))
    output1 = np.array(output1).reshape(-1, 28, 28, 1)
    classifer = joblib.load("python.pk2")
    x = classifer.predict_classes(output1[[0], :])
    if x[0] == 0:
        result = "PREDICTED RESULT IS TSHIRT"
    if x[0]==1:
        result = "PREDICTED RESULT IS TROUSERS"
    if x[0]==2:
        result = "PREDICTED RESULT IS PULLOVER"
    if x[0]==3:
        result = "PREDICTED RESULT IS DRESS"
    if x[0]==4:
        result = "PREDICTED RESULT IS COAT"
    if x[0]==5:
        result = "PREDICTED RESULT IS SANDAL"
    if x[0]==6:
        result = "PREDICTED RESULT IS SHIRT"
    if x[0]==7:
        result = "PREDICTED RESULT IS SNEAKER"
    if x[0]==8:
        result = "PREDICTED RESULT IS BAG"
    else:
        result = "PREDICTED RESULT IS ANKLE SHOE"

    return result

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("save.jpeg"))
        im=cv2.imread("save.jpeg")
        result=process_eval(im)
        return render_template('index.html',result=result)

if __name__ == "__main__":
    app.run()

