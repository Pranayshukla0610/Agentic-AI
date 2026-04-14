from agents.base_agent import BaseAgent
from tools.search_tool import SearchTool

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Researcher Agent",
            goal="Collect and summarize information from the web."
        )
        self.search_tool = SearchTool()

    def execute(self, topic):
        search_results = self.search_tool.search(topic)
        prompt = f"Summarize the following information:\n{search_results}"
        return self.run_llm(prompt)