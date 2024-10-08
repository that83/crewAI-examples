from crewai import Crew
from textwrap import dedent
from research_agents import ResearchAgents
from research_tasks import ResearchTasks

from dotenv import load_dotenv
import os
import re
load_dotenv()

class TripCrew:

  def __init__(self, request, specific_requirements):
    self.request = request
    self.specific_requirements = specific_requirements

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


    crew_create = Crew(
      agents=[request_manager_agent],
      tasks=[create_search_phrases_task],
      verbose=True
    )
    search_phrases = crew_create.kickoff()
    
    print(search_phrases)
    self.search_phrases = search_phrases

    search_and_filter_results_task = tasks.search_and_return_results(
      search_agent, self.search_phrases
    )
    crew_search = Crew(
      agents=[
        search_agent
      ],
      tasks=[search_and_filter_results_task],
      verbose=True
    )
    result_urls = crew_search.kickoff()
    result_urls = remove_duplicate_urls(result_urls)
    self.search_result_urls = result_urls

    scrape_and_save_to_file_task = tasks.scrape_and_save_to_file(
      scrape_agent, self.search_result_urls
    )
    crew_crape = Crew(
      agents=[
        scrape_agent
      ],
      tasks=[scrape_and_save_to_file_task],
      verbose=True
    )
    result = crew_crape.kickoff()
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

def remove_duplicate_urls(input_string):
    lines = input_string.split('\n')
    seen_urls = set()
    result_lines = []
    
    url_pattern = re.compile(r'http[s]?://\S+')
    
    for line in lines:
        match = url_pattern.search(line)
        if match:
            url = match.group(0)
            if url not in seen_urls:
                seen_urls.add(url)
                result_lines.append(line)
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)