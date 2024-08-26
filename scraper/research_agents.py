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
                        model_name=os.environ.get("MODEL_NAME", "gpt-4o"),
                        top_p=0.3)

class ResearchAgents():
  def request_manager_agent(self):
    return Agent(
            role='Keyword Generator',
            goal='Generate relevant keywords based on the user request. Prioritize reputable sources such as Reddit, etc.',
            backstory='An expert in generating keywords based on user requests. Prioritizes reputable sources for better search results.',
            tools=[],
            llm=llm,
            verbose=True
        )
  def search_agent(self):
    return Agent(
            role='Internet Searcher',
            goal='Search for URLs related to the keywords.',
            backstory='An expert in searching for URLs related to keywords.',
            tools=[
                SearchTools.search_internet,
            ],
            llm=llm,
            verbose=True
        )
  
  def scrape_agent(self):
    return Agent(
            role='Data Scraper',
            goal='Scrape data from the final list of URLs.',
            backstory='An expert in scraping data from the final list of URLs.',
            tools=[
                BrowserTools.scrape_and_write_to_file,
            ],
            llm=llm,
            verbose=True
        )
    

  
