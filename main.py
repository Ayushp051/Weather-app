import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
st.title("Weather Website")
base_url = "http://api.weatherapi.com/v1/current.json"
key = key = os.getenv("WEATHER_API_KEY")
location = st.text_input("Please enter the city name")
request_url = f"{base_url}?key={key}&q={location}"

response = requests.get(request_url)
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
    st.subheader(f"You are viewing weather for: {weather_data['location']['name']}, {weather_data['location']['region']}, {weather_data['location']['country']}")
    st.write(f"The local time is {weather_data['location']['localtime']}")

    col1, col2,col3 = st.columns(3)
    with col1:
         st.subheader("Temp in F:")
         st.write(f"{weather_data['current']['temp_f']} Feels like: {weather_data['current']['feelslike_f']}")
         st.subheader("Temp in C:")
         st.write(f"{weather_data['current']['temp_c']} Feels like: {weather_data['current']['feelslike_c']}")

    with col2:
        st.subheader("Current condition:")
        st.write(f"{weather_data['current']['condition']['text']}")
        st.image(f"https:{weather_data['current']['condition']['icon']}")
    with col3:
        st.subheader("Wind Speed:")
        st.write(f"{weather_data['current']['wind_mph']}")
        st.subheader("Wind Direction:")
        st.write(f"{weather_data['current']['wind_dir']}")

else:
    print("fail")

