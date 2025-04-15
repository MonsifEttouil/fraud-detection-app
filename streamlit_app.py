import streamlit as st
import requests

st.title("💳 Détection de Fraude par Carte Bancaire")

st.write("Entrez les informations de transaction :")

data = {}
data["Time"] = st.number_input("Time", value=0.0)
for i in range(1, 29):
    data[f"V{i}"] = st.number_input(f"V{i}", value=0.0)
data["Amount"] = st.number_input("Amount", value=0.0)

if st.button("Prédire"):
    res = requests.post("http://localhost:5000/predict", json=data)
    if res.status_code == 200:
        result = res.json()
        prediction = result["fraud"]
        if prediction == 1:
            st.error("🚨 FRAUDE détectée !")
        else:
            st.success("✅ Transaction légitime")
    else:
        st.error("Erreur dans la prédiction.")
