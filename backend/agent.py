import os
import sys
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
# from backend.calendar_tools import book_meeting
from calendar_tools import book_meeting


# Load environment variables
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Setup Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    api_version="v1beta"  
)


# Tool for booking meeting
tools = [
    Tool(
        name="book_meeting",
        func=book_meeting,
        description="Book a meeting in Google Calendar using title, start time, and end time."
    )
]

# Initialize the conversational agent
conversational_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)
