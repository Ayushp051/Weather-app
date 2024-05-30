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
    st.write(f"Location: {weather_data['location']['name']},{weather_data['location']['region']},{weather_data['location']['country']}")
    
else:
    print("fail")