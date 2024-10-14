import streamlit as st
from datetime import datetime
import time

# Set the page configuration (optional)
st.set_page_config(page_title="Digital Clock", layout="centered")

# Function to extract the current time and day
def get_time():
    current_time = datetime.now().strftime("%H : %M : %S")
    current_day = datetime.today().strftime("%A").upper()[:2]
    return current_time, current_day

# Streamlit interface
st.title("Digital Clock")

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
