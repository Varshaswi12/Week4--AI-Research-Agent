import os
import arxiv
import wikipedia

from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

# -------------------------------
# Tavily Search Tool
# -------------------------------

tavily_tool = TavilySearch(
    max_results=5,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


# -------------------------------
# Wikipedia Tool
# -------------------------------

def search_wikipedia(query: str):
    """Search Wikipedia and return a short summary."""
    try:
        wikipedia.set_lang("en")
        result = wikipedia.summary(query, sentences=5)
        return result
    except Exception:
        return "No Wikipedia information found."


# -------------------------------
# ArXiv Tool
# -------------------------------

def search_arxiv(query: str):
    """Search ArXiv and return summaries of the top papers."""
    try:
        client = arxiv.Client()

        search = arxiv.Search(
            query=query,
            max_results=3,
            sort_by=arxiv.SortCriterion.Relevance,
        )

        papers = []

        for paper in client.results(search):
            papers.append(
                f"""
Title: {paper.title}

Authors: {', '.join(author.name for author in paper.authors)}

Summary:
{paper.summary}
"""
            )

        if not papers:
            return "No research papers found."

        return "\n\n".join(papers)

    except Exception:
        return "Unable to fetch ArXiv papers."