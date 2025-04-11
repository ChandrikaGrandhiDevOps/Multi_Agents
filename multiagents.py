from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.storage.session import AgentSession
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)
finance_agent=Agent(
    name="Finance Agent",
    role="Give Financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions="Use Broad tables to display the data",
    show_tool_calls=True,
    read_tool_call_history=True,
    markdown=True,
)


agent_team=Agent(
    team=[web_agent,finance_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Always include the sources"],
    show_tool_calls=True,
    read_tool_call_history=True,
    markdown=True,
)

agent_team.print_response("Analyze companies like tesla,Amazon and suggest me which one i can buy for long term?")