from crewai import Agent
from langchain_openai import ChatOpenAI

from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools


class TripAgents():
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini"
        )

    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the cities based on the provided sequence',
            backstory='An expert in analyzing travel data to pick ideal destinations',
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True)

    def local_expert(self):
        return Agent(
            role='Local Expert at this cities',
            goal='Provide the BEST insights about the selected cities',
            backstory="""A knowledgeable local guide with extensive information
            about the cities, it's attractions and customs""",
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True)

    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
            packing suggestions for the cities""",
            backstory="""Specialist in travel planning and logistics with 
            decades of experience""",
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate,
            ],
            llm=self.llm,
            verbose=True)
