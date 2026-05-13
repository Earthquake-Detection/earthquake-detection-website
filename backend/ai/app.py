from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import joblib
import pandas as pd


app = Flask(__name__)

model = tf.keras.models.load_model("earthquake_model.h5")

scaler = joblib.load("scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    sample = pd.DataFrame([[
        data['lat'],
        data['lon'],
        data['depth'],
        data['mag']
    ]], columns=['Lat', 'Lon', 'Depth', 'Mag'])

    sample = scaler.transform(sample)

    prediction = model.predict(sample)

    predicted_class = np.argmax(prediction)

    classes = [
        "Mild Earthquake",
        "Moderate Earthquake",
        "Strong Earthquake",
        "Very Strong Earthquake"
    ]

    result = classes[predicted_class]

    return jsonify({
        "prediction": result
    })

if __name__ == '__main__':
    app.run(debug=True)