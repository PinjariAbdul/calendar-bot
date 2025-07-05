from fastapi import FastAPI
from pydantic import BaseModel
from calendar_tools import book_meeting  # adjust path if needed

app = FastAPI()

class EventData(BaseModel):
    title: str
    description: str
    start: str
    end: str

@app.post("/book")
def book_event(event: EventData):
    try:
        print(f"🔧 Incoming booking: {event}")
        link = book_meeting(event.title, event.start, event.end, event.description)
        print(f"✅ Booking success! Link: {link}")
        return {"status": "success", "event_link": link}
    except Exception as e:
        import traceback
        print("🔥 ERROR:", traceback.format_exc())
        return {"status": "error", "message": str(e)}
import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # use PORT env var or fallback
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
