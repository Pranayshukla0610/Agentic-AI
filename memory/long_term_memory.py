import json
import os

class LongTermMemory:
    def __init__(self, path="memory_store.json"):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def save(self, data):
        with open(self.path, "r+") as f:
            content = json.load(f)
            content.append(data)
            f.seek(0)
            json.dump(content, f, indent=4)