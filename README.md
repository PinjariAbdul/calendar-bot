# 📅 AI Calendar Bot – Google Calendar Meeting Scheduler

A conversational AI assistant to schedule meetings directly on Google Calendar. Built with **Streamlit**, **FastAPI**, **LangChain agent**, and **Google Calendar API**.

> ✅ Developed as part of the Internship Challenge by Internshala  
> 🔒 Secure API integration with delegated user and service account

---

## 🚀 Features

- 🤖 Chat-based interface to book meetings
- 🔒 Google Calendar OAuth (via service account with delegated access)
- 📆 Real-time event creation
- 🌐 Backend: FastAPI | Frontend: Streamlit
- 🧠 LLM-powered (Gemini Pro via LangChain Tool Calling)

---

## 🖥️ Tech Stack

| Layer       | Tool |
|-------------|------|
| Backend     | FastAPI |
| Frontend    | Streamlit |
| LLM Agent   | LangChain + Gemini Pro |
| Calendar API| Google Calendar v3 |
| Hosting     | [Railway](https://railway.app) / [Render](https://render.com) / Fly.io |

---

## ⚙️ Environment Setup

### 🔑 Required Files (Not Included in Repo)

You must create the following **secret files locally**:

### 1. `.env` file

```env
CALENDAR_ID=your_calendar_id@group.calendar.google.com
DELEGATED_EMAIL=your_user@gmail.com
