from crewai import Task
from textwrap import dedent
from datetime import date


class ResearchTasks():
  def create_search_phrases(self, agent, request, specific_requirements):
    return Task(description=dedent(f"""
      Purpose of this process is to create search phrases based on the requirements/request. The search phrases will be used to search the internet for relevant information.
      Step 0: Break down the requirements/request into searching keywords. Then, for each keyword, create a search phrase.
      Step 1: Return the list of search phrases (maximum 5 search phrases).
      
      Original Research Request: {request}
      Original Specific Requirements: {specific_requirements}
      """),
      agent=agent,
      backstory='An expert in project management with a strong background in creating search phrases based on requirements and requests.')


  def search_and_return_results(self, agent):
    return Task(description=dedent(f"""
      Purpose of this process is to search the internet using the provided search phrases and filter the search results.
      Step 1: Search the internet using the search phrases.
      Step 2: Return the search results.
      """),
      agent=agent,
      backstory='An expert in project management with a strong background in internet searching.')


  def scrape_and_save_to_file(self, agent):
    return Task(description=dedent(f"""
      Purpose of this process is to scrape the data from the search results and save it to a file.
      Step 0: Use a scraping tool to extract data from the search results. In this step, scraping tool will also save the scraped data to file.
      """),
      agent=agent,
      backstory='An expert in project management with a strong background in using scraping tools.')


  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"
  