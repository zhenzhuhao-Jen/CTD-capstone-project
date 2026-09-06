from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService())
driver.get('https://www.timeanddate.com/weather/')

#print the most popular cities 143 weather
# html route tbody tr td; city name: class'wds'
# Python program to scrape table from website


# Obtain the number of rows in body
rows = len(driver.find_elements(By.XPATH,
    "/html/body/div[5]/section[1]/div/section/div[1]/div/table/tbody/tr"))

# Obtain the number of columns in table
cols = len(driver.find_elements(By.XPATH,
    "/html/body/div[5]/section[1]/div/section/div[1]/div/table/tbody/tr[1]/td"))

# Print rows and columns
#print(rows)
#print(cols)

# creating the list of data for the most popular city weather
city_weather = []

# Printing the data of the table
for r in range(1, rows+1):
    for p in range(1, cols+1):
      
        # obtaining the text from each column of the table
        value = driver.find_element(By.XPATH,
            "/html/body/div[5]/section[1]/div/section/div[1]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]")
        match p % 4:
            case 1:
                city = value.text.strip()
            case 2:
                day_time = value.text.strip()
            case 3:
                weather = value.accessible_name.strip()
            case 0:
                temperature = value.text.strip()
                city_weather.append({"city": city, "day_time": day_time, "weather": weather, "temperature": temperature})

        
       
print(city_weather)

import pandas as pd
df = pd.DataFrame(city_weather)
df.to_csv("popular_city_weather.csv", index=False)


