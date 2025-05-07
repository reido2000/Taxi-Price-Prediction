import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='NYC_Taxi',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load Model
with open('model.pkl', 'rb') as p:
    model = pickle.load(p)

def run():

    st.title('Predict New York Taxi Yellow Price')

    with st.form(key='form_NYC_Taxi'):
        trip_dist = st.slider('trip_distance', 0, 100, 50)
        pas_count = st.selectbox('passenger_count',('1', '2', '3', '4', '5', '6'))
        
        st.markdown('---')
        
        code = st.selectbox('rate_code', ('Standard rate', 'Other'), index = 0)
        payment = st.selectbox('payment_type', ('Credit Card', 'Cash'), index = 1)
        
        submitted = st.form_submit_button('Predict')

    df_inf = {'trip_distance' : trip_dist,
              'passenger_count' : pas_count,
              'rate_code': code,
              'payment_type': payment}

    #Convert to Dataframe pandas
    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)

    if submitted:
        # Predict the new data
        prediction = model.predict(df_inf)
        st.write('# Total Amount : $ ', f'{float(prediction):.2f}')

if __name__ == '__main__':
    run()