import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="📅 Smart Calendar Assistant", layout="centered")

# === Header ===
st.markdown("""
    <style>
        .title {
            font-size: 2.2em;
            font-weight: 700;
            color: #2F4F4F;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.05em;
            color: #666;
            margin-bottom: 25px;
        }
        .footer {
            font-size: 0.9em;
            color: #aaa;
            margin-top: 50px;
            text-align: center;
        }
        .stTextInput>div>input {
            border: 1px solid #ccc;
            padding: 0.4rem;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📅 Smart Calendar Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Easily schedule Google Calendar meetings with custom time input.</div>', unsafe_allow_html=True)

# === Input Fields ===
with st.form("calendar_form"):
    title = st.text_input("📌 Event Title", placeholder="e.g., Team Standup or Doctor Appointment")
    description = st.text_area("📝 Description (optional)", placeholder="Add notes or agenda...", height=100)

    date = st.date_input("📅 Select Date")

    col1, col2 = st.columns(2)
    with col1:
        start_time_str = st.text_input("⏰ Start Time (24h format)", value="10:00", help="Example: 14:30")
    with col2:
        end_time_str = st.text_input("🕒 End Time (24h format)", value="10:30", help="Example: 15:15")

    submitted = st.form_submit_button("✅ Book Meeting")

# === Submit Logic ===
if submitted:
    try:
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.strptime(end_time_str, "%H:%M").time()

        start = datetime.combine(date, start_time).isoformat()
        end = datetime.combine(date, end_time).isoformat()

        payload = {
            "title": title.strip(),
            "description": description.strip(),
            "start": start,
            "end": end
        }

        response = requests.post("http://localhost:8000/book", json=payload)

        if response.status_code == 200 and response.json().get("status") == "success":
            link = response.json()["event_link"]
            st.success("🎉 Meeting booked successfully!")
            st.markdown(f"[🔗 View on Google Calendar]({link})", unsafe_allow_html=True)
        else:
            st.error(f"❌ Booking failed: {response.json().get('message')}")
    except ValueError:
        st.error("⚠️ Invalid time format. Please use HH:MM (24-hour).")
    except Exception as e:
        st.error(f"⚠️ Something went wrong: {str(e)}")

# === Footer ===
st.markdown("""
    <div class="footer">
        Built with ❤️ by Abdul for the Internship Project · FastAPI + Streamlit + Google Calendar API
    </div>
""", unsafe_allow_html=True)
