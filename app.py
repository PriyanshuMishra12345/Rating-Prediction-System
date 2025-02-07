import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

scaler = joblib.load("Scaler.pkl")

st.title("Restaurant Rating Predictions App")

st.caption("This app helps you to predict a restaurant review class")



st.divider()

st.image('https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?cs=srgb&dl=chairs-coffee-shop-drinking-glasses-67468.jpg&fm=jpg', caption='lolllzzzz', use_column_width=True)

averagecost = st.number_input("Please enter the estimated cost for two", min_value=50, max_value=99999, value= 1000, step=200)

tablebooking = st.selectbox("Restaurant has table booking?", ["Yes","NO"])

onlinedelievery = st.selectbox("Restaurant has online booking?",["Yes","No"])

pricerange = st.selectbox("What is the price range(1 Cheapest, 4 Most expensive)",[1,2,3,4,])

predictbutton = st.button("Predict the review!")

st.divider()

model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking=="Yes" else 0

deliverystatus = 1 if onlinedelievery=="Yes" else 0

values = [[averagecost,bookingstatus,deliverystatus,pricerange]]
my_X_values= np.array(values)

X = scaler.transform(my_X_values)

if predictbutton:
    st.snow()

    prediction= model.predict(X)

    st.write(prediction)
