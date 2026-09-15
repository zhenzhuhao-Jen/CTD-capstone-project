import sqlite3
import streamlit as st
import pandas as pd     # Used to work with tabular data
import numpy as np      # Helps generate random numbers
import plotly.express as px  # For interactive charts
import seaborn as sns

#import database
conn = sqlite3.connect('/Users/zhenzhu/python_class/CTD-capstone-project/weather_database.db')
cursor = conn.cursor()
query = """
SELECT * FROM weather
"""
df = pd.read_sql_query(query, conn)

#print(df.tail())
df['city'] = df['city'].str.replace('*', '').str.strip()
df = df.sort_values(by='temperature')
print('the top 10 coldest cities:')
print(df.head(10))

df1 = df.copy()
df1['thermal_label'] = df1['weather'].str.strip('. ').str.split('.').str[-1].str.strip()

df1 = df1.groupby('thermal_label').agg({'temperature': 'mean'}).reset_index()
df1 = df1.sort_values('temperature')
print(df1)



# Main app content starts here
st.title('Weather Dashboard') 
st.subheader('This dashboard shows weather data for the most popular cities from www.timeanddate.com/weather')

# Dropdown menu — user picks one option
options = ["TOP 10 coldest cities", "TOP 10 hottest cities", "Temperature Range by Thermal Descriptor"] 
selected_option = st.selectbox("Choose an option", options, index=0)  

if selected_option == "TOP 10 coldest cities":
    bar_chart = px.bar(df.head(10), x='city', y='temperature', title='TOP 10 coldest cities', 
        labels={'city': 'city', 'temperature': 'Temperature (°F)'})  
    st.plotly_chart(bar_chart, use_container_width=True)
elif selected_option == "TOP 10 hottest cities":
    bar_chart2 = px.bar(df.tail(10), x='city', y='temperature', title='TOP 10 hottest cities', 
        labels={'city': 'city', 'temperature': 'Temperature (°F)'})
    st.plotly_chart(bar_chart2, use_container_width=True)
elif selected_option == "Temperature Range by Thermal Descriptor":
    box_chart = px.box(
        df1, x='thermal_label', y='temperature', 
        title='Temperature Range by Thermal Descriptor', 
        labels={'thermal_label': 'Thermal Descriptor', 'temperature': 'Temperature (°F)'}, 
        color='thermal_label')
    st.plotly_chart(box_chart, use_container_width=True)


