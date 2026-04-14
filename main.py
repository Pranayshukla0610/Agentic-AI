from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearcherAgent
from agents.writer_agent import WriterAgent
from agents.reflection_agent import ReflectionAgent
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

def main():
    topic = input("Enter a research topic: ")

    planner = PlannerAgent()
    researcher = ResearcherAgent()
    writer = WriterAgent()
    reflector = ReflectionAgent()

    short_memory = ShortTermMemory()
    long_memory = LongTermMemory()

    print("\n[1] Planning...")
    plan = planner.execute(topic)
    short_memory.add({"plan": plan})
    print(plan)

    print("\n[2] Researching...")
    summary = researcher.execute(topic)
    short_memory.add({"summary": summary})
    print(summary)

    print("\n[3] Writing Report...")
    report = writer.execute(topic, summary)
    print(report)

    print("\n[4] Reflecting...")
    improved_report = reflector.execute(report)
    print(improved_report)

    long_memory.save({
        "topic": topic,
        "plan": plan,
        "report": improved_report
    })

    print("\n✅ Project completed successfully!")

if __name__ == "__main__":
    main()