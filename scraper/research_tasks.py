from crewai import Task
from textwrap import dedent
from datetime import date


class ResearchTasks():
  def identify_task(self, agent, request, specific_requirements):
    return Task(description=dedent(f"""
      Break down the research request into smaller parts.
      Think of additional useful requirements.
      Chia thành nhiều lần, Search the internet and check the reliability based on the URLs of the search results.
      Skip any search results related to sales, advertising, or service offerings.
      If the search results appear reliable and objective, use a tool to scrape the data and save it to a file.
      Continue this process to scrape as much data as possible.
      The scraped data will be analyzed in another application.

      Original Research Request: {request}
      Original Specific Requirements: {specific_requirements}
      """),
          agent=agent,
          backstory='An expert in project management with a strong background in organizing, internet searching, finding out the reliability of search results, passing URLs to the scraping tool, and saving the data to a file. Continues to scrape as much data as possible, which will be analyzed in another application.')


  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you \$100!"
  