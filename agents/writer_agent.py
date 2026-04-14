from agents.base_agent import BaseAgent

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Writer Agent",
            goal="Create a detailed and structured research report."
        )

    def execute(self, topic, summary):
        prompt = f"""
        Write a detailed report on the topic: {topic}
        using the following summary:
        {summary}

        Include:
        - Introduction
        - Key Insights
        - Applications
        - Challenges
        - Future Scope
        - Conclusion
        """
        return self.run_llm(prompt)