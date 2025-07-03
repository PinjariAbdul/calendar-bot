import streamlit as st
import requests
from datetime import datetime, time

st.title("📅 Calendar Bot – Book a Meeting")

title = st.text_input("Event Title")
description = st.text_area("Event Description")

# Friendly date and time inputs
date = st.date_input("Select Meeting Date")
start_time_input = st.time_input("Start Time", time(10, 0))
end_time_input = st.time_input("End Time", time(10, 30))

if st.button("Book Meeting"):
    # Combine date and time into ISO 8601 string
    start_datetime = datetime.combine(date, start_time_input).isoformat()
    end_datetime = datetime.combine(date, end_time_input).isoformat()

    payload = {
        "title": title,
        "description": description,
        "start": start_datetime,
        "end": end_datetime
    }

    try:
        response = requests.post("http://localhost:8000/book", json=payload)
        if response.status_code == 200:
            st.success("✅ Meeting booked successfully!")
            st.markdown(f"[View on Google Calendar]({response.json()['event_link']})")
        else:
            st.error(f"❌ Failed to book: {response.text}")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
