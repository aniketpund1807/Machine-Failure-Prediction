import streamlit as st
import pickle

st.title("Machine Failure Prediction !")

with open('Machine.pkl','rb') as file:
    model = pickle.load(file)

Footfall = st.number_input("Enter the footfall",0,1000)
Temperature_Mode = st.number_input("Enter the Temperature Mode",0,100)
Quality = st.number_input("Enter the Air Quality",0,100)
USS = st.number_input("Enter the USS",0,100)
CS = st.number_input("Enter the CS",0,100)
VOC = st.number_input("Enter the VOC",0,100)
RPM = st.number_input("Enter the RP",0,100)
IP = st.number_input("Enter the IP",0,100)
Temperature = st.number_input('Enter the Temperature',0,100)

input_data = [[Footfall, Temperature_Mode, Quality, USS, CS, VOC, RPM, IP, Temperature]]

if st.button("Predict"):
    Prediction = model.predict(input_data)

    if Prediction[0] == 0:
        st.write("Machine is not fail")
    
    else:
        st.write("Machine is fail")
