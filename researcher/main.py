from crewai import Crew
from textwrap import dedent
from researcher.research_agents import ResearchAgents
from researcher.research_tasks import ResearchTasks

from dotenv import load_dotenv
load_dotenv()

class TripCrew:

  def __init__(self, request, specific_requirements):
    self.request = request
    self.specific_requirements = specific_requirements

  def run(self):
    agents = ResearchAgents()
    tasks = ResearchTasks()

    request_manager_agent = agents.request_manager_agent()
    technical_expert_agent = agents.technical_expert_agent()
    business_analyst_agent = agents.business_analyst_agent()

    identify_task = tasks.identify_task(
      request_manager_agent,
      self.request,
      self.specific_requirements
    )
    gather_task = tasks.gather_task(
      technical_expert_agent,
      self.request,
      self.specific_requirements
    )
    expand_task = tasks.expand_task(
      business_analyst_agent, 
      self.request,
      self.specific_requirements
    )

    crew = Crew(
      agents=[
        request_manager_agent, technical_expert_agent, business_analyst_agent
      ],
      tasks=[identify_task, gather_task, expand_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
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
