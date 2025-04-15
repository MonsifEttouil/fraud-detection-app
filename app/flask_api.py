from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model/fraud_model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([list(data.values())])
    prediction = model.predict(features)[0]
    return jsonify({"fraud": int(prediction)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
