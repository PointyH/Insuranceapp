import pickle
import numpy as np 
import pandas as pd 
import streamlit as st

with open('model.pkl', 'rb') as file:
    model=pickle.load(file)
with open('text_processor.pkl', 'rb') as file:
    text_processor=pickle.load(file)

st.title('Insurance premium predictor')

age = st.slider('Age (yrs)', 18, 64)
sex = st.selectbox('Sex', ['Male', 'Female'])
bmi = st.slider('BMI', 16, 53)
children = st.slider('Number of children', 0, 5)
smoker = st.selectbox('Smoker?', ['Yes', 'No'])

sex_num, smoker_num = text_processor.transform([[sex,smoker]])[0]
input_data = np.array([age,sex_num,bmi,children,smoker_num]).reshape(1,-1)

prediction = model.predict(input_data)

st.write(f'insurance cost: {prediction}')
