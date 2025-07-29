import streamlit as st
import EDA
import prediction

page = st.selectbox('Navigate To :', ('EDA', 'Predict Taxi Price'))

if page == 'EDA':
    EDA.run()
else:
    prediction.run()