from flask import Flask, request, jsonify
import pandas as pd
import joblib
import sqlite3

app = Flask(__name__)
model = joblib.load('fraud_model.pkl')

# Define the expected feature order
feature_order = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
def save_to_db(data, prediction):
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input TEXT,
            prediction INTEGER
        )
    ''')
    cursor.execute("INSERT INTO predictions (input, prediction) VALUES (?, ?)", (str(data), int(prediction)))
    conn.commit()
    conn.close()
@app.route('/')
def home():
    return "Credit Card Fraud Detection API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        df = df[feature_order]  # reorder columns
        prediction = model.predict(df)
        return jsonify({'fraud': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
