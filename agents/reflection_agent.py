from agents.base_agent import BaseAgent

class ReflectionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Reflection Agent",
            goal="Improve and refine the generated report."
        )

    def execute(self, report):
        prompt = f"Improve the following report and correct any issues:\n{report}"
        return self.run_llm(prompt)