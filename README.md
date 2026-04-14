# 🤖 Agentic AI Research Assistant

An advanced multi-agent AI system that autonomously plans, researches, and generates structured reports on any given topic. This project demonstrates the practical implementation of **Agentic AI** using Python and OpenAI's language models.

## 🚀 Features

- 🧭 Planner Agent for task decomposition
- 🔍 Researcher Agent with web search capability
- 📝 Writer Agent for structured report generation
- 🔎 Reflection Agent for self-improvement
- 🧠 Short-Term and Long-Term Memory
- 🛠️ Tool Integration
- 📦 Modular and Scalable Architecture

## 🏗️ Project Architecture
agentic_ai_project/
│
├── main.py
├── config.py
├── requirements.txt
├── .env (not included)
├── README.md
│
├── agents/
│ ├── base_agent.py
│ ├── planner_agent.py
│ ├── researcher_agent.py
│ ├── writer_agent.py
│ └── reflection_agent.py
│
├── tools/
│ └── search_tool.py
│
├── memory/
│ ├── short_term_memory.py
│ └── long_term_memory.py

## 🛠️ Tech Stack

- Python
- OpenAI API
- DuckDuckGo Search
- Python Dotenv
- Rich (for CLI output)

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/agentic-ai-project.git
cd agentic-ai-project