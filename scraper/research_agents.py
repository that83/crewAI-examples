import os

from crewai import Agent
from langchain_community.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from tools.browser_tools import BrowserTools
#from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
                        openai_api_key=os.environ.get("OPENAI_API_KEY"),
                        temperature=0.1,                        
                        model_name=os.environ.get("MODEL_NAME", "gpt-4"),
                        top_p=0.3)

class ResearchAgents():
  def request_manager_agent(self):
    return Agent(
        role='Request Manager',
        goal='Break down the research request into smaller parts, think of additional useful requirements, search the internet, check the reliability based on the URLs of the search results. If they seem related to sales, advertising, or service offerings, skip them. If they appear reliable and objective, use a tool to scrape the data and save it to a file. Continue this process to scrape as much data as possible. The data will be analyzed in another application.',
        backstory='An expert in project management with a strong background in organizing, internet searching, finding out the reliability of search results, passing URLs to the scraping tool, and saving the data to a file. Continues to scrape as much data as possible, which will be analyzed in another application.',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_write_to_file,
        ],
        llm=llm,
        verbose=True)

  def technical_expert_agent(self):
    return Agent(
        role='Technical Expert',
        goal='Provide in-depth research and answers on specific technical aspects or techniques as requested by the Request Manager.',
        backstory=
        'A specialist in technical research with extensive knowledge in various fields.',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm=llm,
        verbose=True)

  def business_analyst_agent(self):
    return Agent(
        role='Business Analyst',
        goal='Evaluate and critique the responses from the Technical Expert from a business perspective, considering factors such as cost, time, reliability, and providing out-of-the-box ideas for better research outcomes.',
        backstory=
        'An experienced business analyst with a keen eye for cost-benefit analysis, market trends, and innovative business strategies.',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm=llm,
        verbose=True)
