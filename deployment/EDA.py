import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image


def run():

    # Title & Header
    st.title('🚕 New York Yellow Taxi - Price Analysis')
    st.markdown("""
    <style>
    .reportview-container .main .block-container{{
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Gambar Header
    image = Image.open('NYCLogo.jpg')
    st.image(image, caption='New York Yellow Taxi', use_column_width=True)

    # Load Dataset
    try:
        data = pd.read_csv('taxi.csv')
    except FileNotFoundError:
        st.error('The dataset `taxi.csv` could not be found')
        return

    st.markdown('### 🗃️ Dataset Preview')
    st.dataframe(data.head())

    st.markdown('---')

    # Pie Charts: Vendor & Payment Type
    st.markdown('### 📊 Vendor and Payment Type Distribution')

    col1, col2 = st.columns(2)

    with col1:
        vendor_count = data['vendor_id'].value_counts()
        vendor_labels = ['Creative Mobile Tech', 'VeriFone Inc']
        fig1, ax1 = plt.subplots()
        ax1.pie(vendor_count, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title('Vendor Distribution')
        ax1.legend(vendor_labels, loc='best')
        st.pyplot(fig1)

    with col2:
        payment_count = data['payment_type'].value_counts()
        payment_labels = ['Credit Card', 'Cash', 'No Charge', 'Dispute']
        fig2, ax2 = plt.subplots()
        ax2.pie(payment_count, autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')
        ax2.set_title('Payment Type Distribution')
        ax2.legend(payment_labels, loc='best')
        st.pyplot(fig2)

    st.markdown('---')

    # Bar Chart
    st.markdown('### 📈 Distribution by Category')

    option = st.selectbox('Choose a column to display its distribution:', ('rate_code', 'payment_type', 'passenger_count'))

    fig3, ax3 = plt.subplots(figsize=(12, 5))
    sns.countplot(data=data, x=option, ax=ax3, palette='Set2')
    ax3.set_title(f'Distribution based on {option}', fontsize=14)
    st.pyplot(fig3)

    st.markdown('---')

    # Scatter Plot
    st.markdown('### 💵 Trip Distance & Fare Correlation')

    col3, col4 = st.columns(2)

    with col3:
        st.write('#### Fare Amount vs Trip Distance')
        fig4 = px.scatter(data,
                          x='fare_amount',
                          y='trip_distance',
                          color='payment_type',
                          hover_data=['passenger_count', 'rate_code'],
                          title='Fare vs Distance')
        st.plotly_chart(fig4, use_container_width=True)

    with col4:
        st.write('#### Total Amount vs Trip Distance')
        fig5 = px.scatter(data,
                          x='total_amount',
                          y='trip_distance',
                          color='payment_type',
                          hover_data=['passenger_count', 'rate_code'],
                          title='Total vs Distance')
        st.plotly_chart(fig5, use_container_width=True)

    st.markdown('---')
    st.success('Exploratory Data Analysis completed! Head over to the prediction page to try out the model')


if __name__ == '__main__':
    run()