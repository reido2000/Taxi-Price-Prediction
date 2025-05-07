import streamlit as st
import EDA
import prediction

page = st.sidebar.selectbox('Pilih Halaman :', ('EDA', 'Predict Taxi Price'))

if page == 'EDA':
    EDA.run()
else:
    prediction.run()