from crewai import Crew
from textwrap import dedent
from research_agents import ResearchAgents
from research_tasks import ResearchTasks

from dotenv import load_dotenv
import os
load_dotenv()

class TripCrew:

  def __init__(self, request, specific_requirements):
    self.request = request
    self.specific_requirements = specific_requirements
    #self.search_phrases = []
    #self.search_result_urls = []

  def run(self):
    agents = ResearchAgents()
    tasks = ResearchTasks()

    request_manager_agent = agents.request_manager_agent()
    search_agent = agents.search_agent()
    scrape_agent = agents.scrape_agent()

    create_search_phrases_task = tasks.create_search_phrases(
      request_manager_agent,
      self.request,
      self.specific_requirements
    )
    search_and_filter_results_task = tasks.search_and_filter_results(
      search_agent,
      create_search_phrases_task.result
    )

    scrape_and_save_to_file_task = tasks.scrape_and_save_to_file(
      scrape_agent,
      search_and_filter_results_task.result
    )

    crew = Crew(
      agents=[
        request_manager_agent, search_agent, scrape_agent
      ],
      tasks=[create_search_phrases_task, search_and_filter_results_task, scrape_and_save_to_file_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  file_path = "withwebdata.txt"

  if os.path.isfile(file_path):
    with open(file_path, "w") as file:
      file.write("")
  print("## Welcome to Research Crew")
  print('-------------------------------')
  request = input(
    dedent("""
      What do you want to research?
    """))
    
  specific_requirements = input(
    dedent("""
      Any specific requirements?
    """))
  
  trip_crew = TripCrew(request, specific_requirements)
  result = trip_crew.run()
  print("\n\n########################")
  print("## Here is your result:")
  print("########################\n")
  print(result)
