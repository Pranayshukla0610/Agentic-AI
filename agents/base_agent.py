from abc import ABC, abstractmethod
from openai import OpenAI
from config import Config

class BaseAgent(ABC):
    def __init__(self, role, goal):
        self.role = role
        self.goal = goal
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def run_llm(self, prompt):
        response = self.client.chat.completions.create(
            model=Config.MODEL_NAME,
            messages=[
                {"role": "system", "content": f"You are a {self.role}. {self.goal}"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass