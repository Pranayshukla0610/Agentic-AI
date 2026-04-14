from duckduckgo_search import DDGS

class SearchTool:
    def search(self, query, max_results=5):
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r["body"])
        return " ".join(results)