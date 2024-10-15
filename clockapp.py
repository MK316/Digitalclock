import streamlit as st
from datetime import datetime
import time
import requests
from streamlit_lottie import st_lottie

# Set the page configuration (optional)
st.set_page_config(page_title="Digital Clock", layout="centered")

# Function to load a Lottie animation from a file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return file.read()

# Function to extract the current time and day
def get_time():
    current_time = datetime.now().strftime("%H : %M : %S")
    current_day = datetime.today().strftime("%A").upper()[:2]
    return current_time, current_day

# Load Lottie animation
lottie_animation = load_lottiefile("Animation - 1728988122037.lottie")

# Streamlit interface using columns to place the title and Lottie animation side by side
col1, col2 = st.columns([3, 1])  # Adjust the ratio as needed

with col1:
    st.title("Digital Clock")

with col2:
    st_lottie(lottie_animation, height=100, key="digital_clock")  # Set height appropriately

# Display time
time_placeholder = st.empty()  # Placeholder for dynamic updates
day_placeholder = st.empty()   # Placeholder for the day

while True:
    # Get current time and day
    current_time, current_day = get_time()
    
    # Display the clock and day
    time_placeholder.markdown(f"<h1 style='text-align: center;'>{current_time}</h1>", unsafe_allow_html=True)
    day_placeholder.markdown(f"<h2 style='text-align: center;'>{current_day} |</h2>", unsafe_allow_html=True)
    
    # Refresh every second
    time.sleep(1)
