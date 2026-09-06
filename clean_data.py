#clean the data
#check for missing values, data type and duplicates
import pandas as pd
df = pd.read_csv('/Users/zhenzhu/python_class/CTD-capstone-project/popular_city_weather.csv')
df_new = df.copy()

df_new.info()

total_duplicates = df_new.duplicated().sum()
print(total_duplicates)
# no duplicates; has missing values; need to transform the temperature column datatype to int; 
print(df_new.isna().sum())
df_new = df_new.dropna()
df_new.info()


# Remove '°F' and strip extra spaces
df_new['temperature'] = df_new['temperature'].str.replace('°F', '', regex=True).str.strip()

# Optional: Convert the cleaned column to numbers
df_new['temperature'] = pd.to_numeric(df_new['temperature'])
df_new.info()

# save dataframe to csv file
df_new.to_csv("cleaned_popular_city_weather.csv", index=False)

import sqlite3
conn = sqlite3.connect('weather_database.db')
df_new.to_sql('weather', conn, if_exists='replace', index=False)
conn.close()
