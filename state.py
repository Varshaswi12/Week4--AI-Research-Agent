from typing import List
from typing_extensions import TypedDict


class ResearchState(TypedDict):
    question: str

    tools: List[str]

    tavily_results: List[str]
    wikipedia_results: List[str]
    arxiv_results: List[str]
    github_results: List[dict]

    combined_results: str

    summary: str