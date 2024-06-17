import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from urllib.parse import quote_plus

class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    api_key = os.environ['SCRAPINGFISH_API_KEY']
    url = quote_plus(website)
    response = requests.get(f"https://scraping.narf.ai/api/v1/?api_key={api_key}&url={url}")

    elements = partition_html(text=response.content)
    print(f"[debug][SCRAPINGFISH] {elements}")  # print out the results for debugging
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
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
    return "\n\n".join(summaries)
