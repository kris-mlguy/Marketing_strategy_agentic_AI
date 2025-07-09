from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool

@CrewBase
class MarketingStrategyCrew():
	"""MarketingStrategyCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

	# @before_kickoff # Optional hook to be executed before the crew starts
	# def pull_data_example(self, inputs):
	# 	# Example of pulling data from an external API, dynamically changing the inputs
	# 	inputs['extra_data'] = "This is extra data"
	# 	return inputs

	# @after_kickoff # Optional hook to be executed after the crew has finished
	# def log_results(self, output):
	# 	# Example of logging results, dynamically changing the output
	# 	print(f"Results: {output}")
	# 	return output

	@agent
	def senior_market_researcher(self) -> Agent:
		# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
		return Agent(
			config=self.agents_config['senior_market_researcher'],
			tools=[SerperDevTool()],
			verbose=True,
			# llm=llm
		)

	@agent
	def senior_marketing_analyst(self) -> Agent:
		# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
		return Agent(
			config=self.agents_config['senior_marketing_analyst'],
			verbose=True,
			# llm=llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file='outputs/research.md'
		)

	@task
	def analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyst_task'],
			output_file='outputs/report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MarketingStrategyCrew crew"""
		# You can add knowledge sources here
		# knowledge_path = "user_preference.txt"
		# sources = [
		# 	TextFileKnowledgeSource(
		# 		file_path="knowledge/user_preference.txt",
		# 		metadata={"preference": "personal"}
		# 	),
		# ]

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
			# knowledge_sources=sources, # In the case you want to add knowledge sources
		)
