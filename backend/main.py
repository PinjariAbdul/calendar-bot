# from fastapi import FastAPI
# from pydantic import BaseModel
# from agent import conversational_agent
# from calendar_tools import book_meeting  # Import the function

# app = FastAPI()

# class Query(BaseModel):
#     input: str

# @app.post("/book")
# def book():
#     from backend.calendar_tools import book_meeting
#     book_meeting()
#     return {"message": "Meeting booked!"}

# # ✅ Add this new route
# class EventData(BaseModel):
#     title: str
#     description: str
#     start: str  # ISO format like 2025-07-04T10:00:00+05:30
#     end: str

# @app.post("/book")
# def book_event(event: EventData):
#     link = book_meeting(event.title, event.start, event.end, event.description)
#     return {"status": "success", "event_link": link}
from fastapi import FastAPI
from pydantic import BaseModel
from calendar_tools import book_meeting  # adjust path if needed

app = FastAPI()

class EventData(BaseModel):
    title: str
    description: str
    start: str  # "2025-07-04T10:00:00+05:30"
    end: str    # "2025-07-04T10:30:00+05:30"

@app.post("/book")
def book_event(event: EventData):
    try:
        link = book_meeting(event.title, event.start, event.end, event.description)
        return {"status": "success", "event_link": link}
    except Exception as e:
        return {"status": "error", "message": str(e)}
