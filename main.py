import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle


app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl','rb'))


@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    #print(int_features) 
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
	#prediction = model.predict(int_features)
    print(prediction[0])

    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Fare Prediction {}".format(prediction[0]))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    #print(data) 
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
