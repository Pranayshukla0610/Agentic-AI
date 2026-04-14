from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Planner Agent",
            goal="Break down a research topic into actionable steps."
        )

    def execute(self, topic):
        prompt = f"Create a step-by-step research plan for the topic: {topic}"
        return self.run_llm(prompt)