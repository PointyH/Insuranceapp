{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7c183364-a948-443e-85a3-9f677da0c62c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'st' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[20]\u001b[39m\u001b[32m, line 11\u001b[39m\n\u001b[32m      8\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[33m'\u001b[39m\u001b[33mtext_processor.pkl\u001b[39m\u001b[33m'\u001b[39m, \u001b[33m'\u001b[39m\u001b[33mrb\u001b[39m\u001b[33m'\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[32m      9\u001b[39m     text_processor=pickle.load(file)\n\u001b[32m---> \u001b[39m\u001b[32m11\u001b[39m \u001b[43mst\u001b[49m.title(\u001b[33m'\u001b[39m\u001b[33mInsurance premium predictor\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m     13\u001b[39m age = st.slider(\u001b[33m'\u001b[39m\u001b[33mAge (yrs)\u001b[39m\u001b[33m'\u001b[39m, \u001b[32m18\u001b[39m, \u001b[32m64\u001b[39m)\n\u001b[32m     14\u001b[39m sex = st.selectbox(\u001b[33m'\u001b[39m\u001b[33mSex\u001b[39m\u001b[33m'\u001b[39m, [\u001b[33m'\u001b[39m\u001b[33mMale\u001b[39m\u001b[33m'\u001b[39m, \u001b[33m'\u001b[39m\u001b[33mFemale\u001b[39m\u001b[33m'\u001b[39m])\n",
      "\u001b[31mNameError\u001b[39m: name 'st' is not defined"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import numpy as np \n",
    "import pandas as pd \n",
    "#import streamlit as st\n",
    "\n",
    "with open('model.pkl', 'rb') as file:\n",
    "    model=pickle.load(file)\n",
    "with open('text_processor.pkl', 'rb') as file:\n",
    "    text_processor=pickle.load(file)\n",
    "\n",
    "st.title('Insurance premium predictor')\n",
    "\n",
    "age = st.slider('Age (yrs)', 18, 64)\n",
    "sex = st.selectbox('Sex', ['Male', 'Female'])\n",
    "bmi = st.slider('BMI', 16, 53)\n",
    "children = st.slider('Number of children', 0, 5)\n",
    "smoker = st.selectbox('Smoker?', ['Yes', 'No'])\n",
    "\n",
    "sex_num, smoker_num = text_processor.transform([[sex,smoker]])[0]\n",
    "input_data = np.array([age,sex_num,bmi,children,smoker_num]).reshape(1,-1)\n",
    "\n",
    "prediction = model.predict(input_data)\n",
    "\n",
    "st.write(f'insurance cost: {prediction}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fadf7fc-ae06-48c3-824f-a60475805007",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
