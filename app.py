from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__)


model = joblib.load('insurance_cost_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        age = int(request.form['age'])
        gender = request.form['gender']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        
        gender = 1 if gender == 'male' else 0  
        smoker = 1 if smoker == 'yes' else 0  

        
        region_northwest = 1 if region == 'northwest' else 0
        region_southeast = 1 if region == 'southeast' else 0
        region_southwest = 1 if region == 'southwest' else 0

       
        features = np.array([age, gender, bmi, children, smoker, region_northwest, region_southeast, region_southwest]).reshape(1, -1)

       
        prediction = model.predict(features)
        output = round(prediction[0], 2)

        
        return render_template('index.html', prediction_text=f'Predicted Insurance Cost: ${output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)