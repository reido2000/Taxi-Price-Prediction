import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image


def run():

    #Membuat title
    st.title('New York Taxi Yellow Price')

    #Membuat subheader
    st.subheader('Exploratory Data Analysis dari dataset NYC Taxi')

    #Menambahkan Gambar
    image = Image.open('YellowTaxi.jpg')
    st.image(image, caption='Yellow Taxi')

    #Menampilkan DataFrame
    data = pd.read_csv('taxi.csv')
    st.write('#### Dataset Preview')
    st.dataframe(data)

    # Membuat column
    col1, col2 = st.columns([1,1])
    
    # Column 1
    with col1:
        # Membuat pie plot
        vendor_count = data['vendor_id'].value_counts()

        # Ganti angka 1 dan 2 dengan label yang sesuai
        vendor_labels = ['Creative Mobile Tech', 'VeriFone Inc']

        st.write('#### Plot Payment Type')
        fig = plt.figure(figsize=(6, 6))
        vendor_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, labels=None)
        plt.title('Vendor')
        plt.ylabel('')
        plt.legend(vendor_labels, title='vendor', loc='upper left', bbox_to_anchor=(1, 1))
        st.pyplot(fig)

    # Column 2
    with col2:
        # Membuat pie plot
        payment_type_count = data['payment_type'].value_counts()

        #label
        payment_type_labels = ['Cash', 'Credit Card', 'No Charge', 'Dispute']

        st.write('#### Plot Payment Type')
        fig = plt.figure(figsize=(6, 6))
        payment_type_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, labels=None)
        plt.title('Payment Type')
        plt.ylabel('')
        plt.legend(payment_type_labels, title='Payment Type', loc='upper left', bbox_to_anchor=(1.1, 1))
        st.pyplot(fig)


    #Membuat Bar Chart
    st.write('#### Bar Chart ')
    option = st.selectbox('pilih column: ', ('rate_code','payment_type', 'passenger_count'))
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x=option, data=data)
    st.pyplot(fig)

    #Membuat plot menggunakan plotly
    st.write('#### Fare Amount v Trip Distance')
    fig = px.scatter(data, x='fare_amount', y='trip_distance', hover_data=['passenger_count', 'payment_type'])
    st.plotly_chart(fig)

    #Membuat plot menggunakan plotly
    st.write('#### Total Amount v Trip Distance')
    fig = px.scatter(data, x='total_amount', y='trip_distance', hover_data=['passenger_count', 'payment_type'])
    st.plotly_chart(fig)


if __name__ == '__main__':
    run()