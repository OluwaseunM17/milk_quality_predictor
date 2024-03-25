import streamlit as st
import pickle
import pandas as pd
from PIL import Image

img = Image.open("pexels-samer-d-1210005.jpg")
model = pickle.load(open("milk_grade.pkl","rb"))

st.title("Milk Quality Predictor")
st.image(img)
st.sidebar.header("Milk Data")

def milk_report():
    pH = st.sidebar.slider("Please Select pH of milk", 1.0, 14.0, 0.1)
    temperature = st.sidebar.number_input("Enter Temperature in Celsius", 1, 100)
    taste = st.sidebar.selectbox("Select taste",("Good", "Bad"))
    if (taste == "Good"):
        Taste = 1
    else:
        Taste = 0
    odor = st.sidebar.selectbox("Select Odor",("Good","Bad"))
    if (odor == "Good"):
        Odor = 1
    else:
        Odor = 0
    fat = st.sidebar.selectbox("Select fat content",("low","high"))
    if (fat == "High"):
        Fat = 1
    else:
        Fat = 0
    turbidity = st.sidebar.selectbox("Select level of Turbidity",("Low","High"))
    if (turbidity == "High"):
        Turbidity = 1
    else:
        Turbidity = 0
    user_report_data = {
        'pH':pH,
        'Temprature':temperature,
        'Taste':Taste,
        'Odor':Odor,
        'Fat ':Fat,
        'Turbidity':Turbidity
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data
info=milk_report()

st.subheader("Milk Data Summary")
st.write(info)

quality=model.predict(info)
if (quality==0):
    st.subheader("This Milk's Quality is low")
elif(quality==1):
    st.subheader("This Milk's quality is medium")
else:
    st.subheader("This Milk's Quality is High")

