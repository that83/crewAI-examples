from crewai import Task
from textwrap import dedent
from datetime import date


class ResearchTasks():
  def identify_task(self, agent, request, specific_requirements):
    return Task(description=dedent(f"""
      Purpose of this process to scrape as much data as possible. The scraped data will be saved to file and analyzed in another application.
      Step 0: Break down the requirements/request into searching keywords. Then, for each keyword, perform the following steps:
      Step 1: Search the internet and check the reliability based on the URLs of the search results.
      Step 2: Pick the search results that seem reliable and objective (Skip any related to sales, advertising, or service offerings.)
      Step 3: Use tool to scrape the data of Step 2's url(s) and save it to a file.                             
      Step 4: After obtaining the results, quickly check its "Snippet", think of additional useful requirements. Loop back to Step 0 until you can not think of any more keywords.

      Original Research Request: {request}
      Original Specific Requirements: {specific_requirements}
      """),
      agent=agent,
      backstory='An expert in project management with a strong background in organizing, internet searching, finding out the reliability of search results, passing URLs to the scraping tool, and saving the data to a file. Continues to scrape as much data as possible, which will be analyzed in another application.')


  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you \$100!"
  