from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class CrewaiFruadDetection():
    """CrewaiFruadDetection crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def transaction_analyzer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transaction_analyzer_agent'], 
            verbose=True
        )

    @agent
    def pattern_detector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pattern_detector_agent'],
            verbose=True
        )

    @agent
    def explanation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['explanation_agent'],
            verbose=True
        )

    @task
    def transaction_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['transaction_analysis_task'], 
        )

    @task
    def pattern_detection_task(self) -> Task:
        return Task(
            config=self.tasks_config['pattern_detection_task'], 
        )

    @task
    def fraud_explanation_task(self) -> Task:
        return Task(
            config=self.tasks_config['fraud_explanation_task'], 
            output_file='blobs/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiFruadDetection crew"""


        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            trace=True
        )
