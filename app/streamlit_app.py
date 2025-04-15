import streamlit as st
import pickle
import sqlite3
import pandas as pd

model = pickle.load(open("model/fraud_model.pkl", "rb"))

st.title("Credit Card Fraud Detection")

with st.form("prediction_form"):
    time = st.number_input("Time", value=0.0)
    amount = st.number_input("Amount", value=0.0)
    features = [st.number_input(f"V{i}", value=0.0) for i in range(1, 29)]
    submit = st.form_submit_button("Predict")

if submit:
    input_data = [time] + features + [amount]
    prediction = model.predict([input_data])[0]

    # Affiche résultat
    st.success(f"Prediction: {'Fraud' if prediction == 1 else 'Not Fraud'}")

    # Stocker dans SQLite
    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO predictions (result) VALUES (?)", (int(prediction),))
    conn.commit()
    conn.close()
