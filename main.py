from flask import Flask, render_template, request
import numpy as np
import pickle
import logging
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
@app.route('/main')
def main():
    image_url = 'lung.jpg'
    return render_template('main.html', image_url=image_url)

@app.route('/form')
def index():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    # Retrieve form data
    # Retrieve form data with validation
    try:
        name = request.form['name']
        GENDER = int(request.form['gender'])
        AGE = int(request.form['age'])
        SMOKING = int(request.form['smoking'])
        YELLOW_FINGERS = int(request.form['yf'])
        ANXIETY = int(request.form['anxiety'])
        PEER_PRESSURE = int(request.form['pp'])
        CHRONIC_DISEASE = int(request.form['cd'])
        FATIGUE = int(request.form['fatigue'])
        ALLERGY = int(request.form['allergy'])
        WHEEZING = int(request.form['wheezing'])
        ALCOHOL = int(request.form['alcohol'])
        COUGHING = int(request.form['coughing'])
        SHORTNESS_BREATH = int(request.form['sb'])
        SWALLOWING_DIFFICULTY = int(request.form['sd'])
        CHEST_PAIN = int(request.form['cp'])
    except (ValueError, KeyError) as e:
        logging.error(f"Error retrieving form data: {e}")
        return "Invalid input data", 400

    # Load the model
    #loaded_model = pickle.load(open('model.pkl', 'rb'))
    # Load the model with error handling
    try:
        if not os.path.exists('model.pkl'):
            logging.error("Model file not found.")
            return "Model file not found", 500

        loaded_model = pickle.load(open('model.pkl', 'rb'))
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        return "Error loading model", 500

    # Prepare the input data for prediction
    input_data = np.array([[GENDER, AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING, ALCOHOL,COUGHING,SHORTNESS_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])  # Add other input fields as needed

    # Make the prediction
  try:
    prediction = loaded_model.predict(input_data)

        # Determine the prediction label
    if prediction[0] == 0:
        result = f"{name}, you do not have Lung Cancer"
    else:
        result = f"{name}, you have Lung Cancer"
  except Exception as e:
    logging.error(f"Error making prediction: {e}")
    return "Error during prediction", 500

return render_template('result.html', result=result, name=name)

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode
