from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


agent=Agent(
    model=Groq(id="llama3-70b-8192"),
    description="You are an assistance please replay based on the questions",
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response("who are is the indian cricket team and give me there names?")