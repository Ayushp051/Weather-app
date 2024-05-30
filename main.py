import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
st.title("Weather Website🌤️")
base_url = "http://api.weatherapi.com/v1/current.json"
key = key = os.getenv("WEATHER_API_KEY")
location = st.text_input("Please enter the city name")
request_url = f"{base_url}?key={key}&q={location}"

response = requests.get(request_url)
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
    
    st.subheader("You are viewing weather for:")
    st.subheader(f":green[{weather_data['location']['name']}], :green[{weather_data['location']['region']}], :green[{weather_data['location']['country']}]")
    st.write(f"The local time is :violet[{weather_data['location']['localtime']}]")
    st.write(f"Coordinates: :violet[{weather_data['location']['lat']}] lat, :violet[{weather_data['location']['lon']}] lon")

    col1, col2,col3 = st.columns(3)
    with col1:
        st.subheader(":blue[Temp in F:]")
        st.subheader(f"{weather_data['current']['temp_f']} ")
        st.write(f"Feels like: {weather_data['current']['feelslike_f']}")
        st.subheader(":blue[Temp in C:]")
        st.subheader(f"{weather_data['current']['temp_c']} ")
        st.write(f"Feels like: {weather_data['current']['feelslike_c']}")

    with col2:
        st.subheader(":blue[Current condition:]")
        st.write(f"{weather_data['current']['condition']['text']}")
        st.image(f"https:{weather_data['current']['condition']['icon']}")
        st.subheader(":blue[Expected Rain:]")
        st.subheader(f"{weather_data['current']['precip_in']} in")
    with col3:
        st.subheader(":blue[Wind Speed:]")
        st.subheader(f"{weather_data['current']['wind_mph']} MPH")
        st.subheader(":blue[Wind Direction:]")
        st.subheader(f"{weather_data['current']['wind_dir']}")
        st.subheader(":blue[Humidity:]")
        st.subheader(f"{weather_data['current']['humidity']}%")

else:
    print("fail")

