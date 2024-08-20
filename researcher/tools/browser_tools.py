import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from urllib.parse import quote_plus
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
                        openai_api_key=os.environ.get("OPENAI_API_KEY"),
                        temperature=0.1,                        
                        model_name=os.environ.get("MODEL_NAME", "gpt-3.5-turbo-1106"),
                        top_p=0.3)

class BrowserTools():

  @tool("Scrape website(s) content")
  def scrape_and_summarize_website(websites):
    """Input Url(s) of website(s) to scrape and summarize its content"""
    print(f"[debug][SCRAPINGFISH is called with:] {websites}")  # print out the results for debugging
    api_key = os.environ['SCRAPINGFISH_API_KEY']
    # If websites is a string, convert it to a list
    if isinstance(websites, str):
      websites = websites.split(",")
    summaries = ""
    # Iterate over the list of websites
    for website in websites:
      url = quote_plus(website.strip().strip('"').replace("'", ""))
      print(f"[debug][requesting url:] {url}") 
      response = requests.get(f"https://scraping.narf.ai/api/v1/?api_key={api_key}&url={url}")

      elements = partition_html(text=response.content)
    
      content = "\n\n".join([str(el) for el in elements])
      print(f"[debug][content return: ] {content}")  # print out the results for debugging
      #content = [content[i:i + 16000] for i in range(0, len(content), 16000)]
      summaries.append(f"Content scrapped from website {website} :\n")
      summaries.append(content)
      #for chunk in content:
      #  summaries.append(chunk)
    print(f"[debug][rephrases return: ] {summaries}")  # print out the results for debugging
    return summaries
