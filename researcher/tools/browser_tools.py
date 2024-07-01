import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from urllib.parse import quote_plus

class BrowserTools():

  @tool("Scrape website(s) content")
  def scrape_and_summarize_website(websites):
    """Input Url(s) of website(s) to scrape and summarize its content"""
    print(f"[debug][SCRAPINGFISH is called with:] {websites}")  # print out the results for debugging
    api_key = os.environ['SCRAPINGFISH_API_KEY']
    # If websites is a string, convert it to a list
    if isinstance(websites, str):
      websites = [websites]
    summaries = []
    # Iterate over the list of websites
    for website in websites:
      url = quote_plus(website)
      response = requests.get(f"https://scraping.narf.ai/api/v1/?api_key={api_key}&url={url}")

      elements = partition_html(text=response.content)
    
      content = "\n\n".join([str(el) for el in elements])
      print(f"[debug][content return: ] {content}")  # print out the results for debugging
      content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
      
      for chunk in content:
        agent = Agent(
            role='Principal Researcher',
            goal=
            'Do amazing researches and summaries based on the content you are working with',
            backstory=
            "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
            allow_delegation=False)
        task = Task(
            agent=agent,
            description=
            f'Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
        )
        summary = task.execute()
        summaries.append(summary)
    print(f"[debug][summaries return: ] {summaries}")  # print out the results for debugging
    return "\n\n".join(summaries)
