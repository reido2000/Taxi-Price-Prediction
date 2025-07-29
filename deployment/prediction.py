import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image

st.set_page_config(
    page_title='NYC Taxi Price Predictor',
    layout='wide',
    initial_sidebar_state='expanded',
    page_icon='🚕'
)

# Load Model
with open('model.pkl', 'rb') as p:
    model = pickle.load(p)

def run():
    st.title('🚖 New York Taxi Fare Predictor')
    st.markdown('Use the form below to predict the total fare of a taxi trip in New York')

    st.markdown('---')
    
    # Gambar atau header tambahan
    image = Image.open('NYC.jpg')
    st.image(image, caption='Yellow Taxi NYC', use_column_width=True)

    st.markdown('### ✍️ Input Travel Details')

    # Form Input
    with st.form(key='form_NYC_Taxi'):
        col1, col2 = st.columns(2)

        with col1:
            trip_dist = st.slider('🛣️ Trip Distance (miles)', 0, 100, 2)
            pas_count = st.selectbox('👥 Number of Passengers', ('1', '2', '3', '4', '5', '6'))

        with col2:
            rate_code = st.selectbox('💲 Rate Code', ('Standard rate', 'Other'))
            payment_type = st.selectbox('💳 Payment Type', ('Credit Card', 'Cash'))

        submitted = st.form_submit_button('🚕 Predicted Total Fare')

    # DataFrame
    df_inf = pd.DataFrame([{
        'trip_distance': trip_dist,
        'passenger_count': pas_count,
        'rate_code': rate_code,
        'payment_type': payment_type
    }])

    st.markdown('#### 🔎 Your Input Summary')
    st.dataframe(df_inf)

    if submitted:
        with st.spinner('🔄 Calculating prediction...'):
            time.sleep(1) 
            prediction = model.predict(df_inf)
            pred_value = float(prediction[0])

        st.markdown('---')
        st.success('✅ Prediction completed successfully!')

        st.metric(label='💰 Predicted Total Fare (USD)', value=f'${pred_value:,.2f}')

        # Ganti st.balloons() dengan notifikasi
        st.toast('🎉 The prediction has been displayed successfully!')

        st.markdown('🚦 Use this prediction result to estimate the fare before taking a taxi. Make sure to also consider other real-world factors such as tolls and tips')

if __name__ == '__main__':
    run()