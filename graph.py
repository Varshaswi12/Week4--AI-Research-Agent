from langgraph.graph import StateGraph, START, END

from state import ResearchState

from nodes import (
    planner_node,
    tavily_node,
    wikipedia_node,
    arxiv_node,
    github_node,
    merge_node,
    analyze_node,
    summarize_node
)

builder = StateGraph(ResearchState)

# -------------------------
# Nodes
# -------------------------

builder.add_node("planner", planner_node)
builder.add_node("tavily", tavily_node)
builder.add_node("wikipedia", wikipedia_node)
builder.add_node("arxiv", arxiv_node)
builder.add_node("github", github_node)
builder.add_node("merge", merge_node)
builder.add_node("analyze", analyze_node)
builder.add_node("summarize", summarize_node)

# -------------------------
# Edges
# -------------------------

builder.add_edge(START, "planner")

builder.add_edge("planner", "tavily")
builder.add_edge("tavily", "wikipedia")
builder.add_edge("wikipedia", "arxiv")
builder.add_edge("arxiv", "github")
builder.add_edge("github", "merge")
builder.add_edge("merge", "analyze")
builder.add_edge("analyze", "summarize")
builder.add_edge("summarize", END)

graph = builder.compile()