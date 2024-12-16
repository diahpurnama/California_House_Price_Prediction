import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor

# Change the working directory to the folder where the model is stored
os.chdir(r'C:\Users\diyah_l0lko0w\OneDrive\Documents\Capstone Project 3')

# Load the saved model
model = pickle.load(open('Model_RandomForest.sav', 'rb'))

# Define the column names based on the features used in the model
column_names = [
    'ocean_proximity', 'median_income', 'housing_median_age',
    'rooms_per_household', 'population_per_household', 'bedrooms_per_room', 'population'
]

# App title
st.title('California Housing Price Prediction')

# Input form for the user
ocean_proximity = st.selectbox('Select Ocean Proximity', ['NEAR BAY', 'NEAR OCEAN', 'INLAND', 'ISLAND'])
median_income = st.number_input('Enter Median Income', min_value=0.0, step=0.1)
housing_median_age = st.number_input('Enter Median Housing Age', min_value=0, step=1)
rooms_per_household = st.number_input('Enter Rooms per Household', min_value=0.0, step=0.1)
population_per_household = st.number_input('Enter Population per Household', min_value=0, step=1)
bedrooms_per_room = st.number_input('Enter Bedrooms per Room', min_value=0.0, step=0.1)
population = st.number_input('Enter Population', min_value=0, step=1) 

# Process the input into a pandas DataFrame suitable for model input
input_data = pd.DataFrame([[ocean_proximity, median_income, housing_median_age, rooms_per_household,
                            population_per_household, bedrooms_per_room, population]],
                          columns=column_names)


# Make a prediction
if st.button('Predict Price'):
    prediction = model.predict(input_data)
    st.write(f'Predicted House Price: ${prediction[0]:,.2f}')
