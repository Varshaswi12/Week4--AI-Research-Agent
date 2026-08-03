import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from state import ResearchState
from tools import tavily_tool, search_wikipedia, search_arxiv
from github_tools import search_github

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

# ----------------------------------------------------
# Planner Node
# ----------------------------------------------------
def planner_node(state: ResearchState):

    print("🧠 Planning research strategy...")

    prompt = f"""
You are an AI Research Planner.

Research Question:
{state["question"]}

Available tools:

- tavily (latest web information)
- wikipedia (background knowledge)
- arxiv (research papers)
- github (open-source implementations)

Choose ONLY the tools required.

Return ONLY a comma-separated list.

Examples:
tavily,wikipedia

or

tavily,arxiv,github
"""

    response = llm.invoke(prompt)

    tools = [
        tool.strip().lower()
        for tool in response.content.split(",")
        if tool.strip()
    ]

    print("Selected Tools:", tools)

    return {
        "tools": tools
    }
# ----------------------------------------------------
# Tavily Search
# ----------------------------------------------------
def tavily_node(state: ResearchState):

    if "tavily" not in state["tools"]:
        print("⏭ Skipping Tavily")
        return {
            "tavily_results": []
        }

    print("🌐 Searching latest web...")

    try:
        results = tavily_tool.invoke({"query": state["question"]})
    except Exception:
        results = tavily_tool.invoke(state["question"])

    output = []

    if isinstance(results, list):

        for item in results:

            if isinstance(item, dict):

                output.append(item.get("content", ""))

    return {

        "tavily_results": output

    }


# ----------------------------------------------------
# Wikipedia
# ----------------------------------------------------
def wikipedia_node(state: ResearchState):

    if "wikipedia" not in state["tools"]:
        print("⏭ Skipping Wikipedia")
        return {
            "wikipedia_results": []
        }

    print("📚 Searching Wikipedia...")

    result = search_wikipedia(state["question"])

    return {

        "wikipedia_results": [result]

    }


# ----------------------------------------------------
# ArXiv
# ----------------------------------------------------
def arxiv_node(state: ResearchState):

    if "arxiv" not in state["tools"]:
        print("⏭ Skipping ArXiv")
        return {
            "arxiv_results": []
        }

    print("📄 Searching Research Papers...")

    result = search_arxiv(state["question"])

    return {

        "arxiv_results": [result]

    }


# ----------------------------------------------------
# GitHub
# ----------------------------------------------------
def github_node(state: ResearchState):

    if "github" not in state["tools"]:
        print("⏭ Skipping GitHub")
        return {
            "github_results": []
        }

    print("💻 Searching GitHub Repositories...")

    repos = search_github(state["question"])

    return {

        "github_results": repos

    }
# ----------------------------------------------------
# Merge Results
# ----------------------------------------------------
def merge_node(state: ResearchState):

    print("🔗 Combining all sources...")

    github_text = ""

    for repo in state["github_results"]:

        github_text += f"""
Repository: {repo.get("name")}

Description:
{repo.get("description")}

⭐ Stars: {repo.get("stars")}

💻 Language: {repo.get("language")}

🔗 Repository:
{repo.get("url")}

----------------------------------------------------
"""

    combined = f"""
==============================
🌐 LATEST WEB INFORMATION
==============================

{"".join(state["tavily_results"])}

==============================
📚 WIKIPEDIA
==============================

{"".join(state["wikipedia_results"])}

==============================
📄 RESEARCH PAPERS
==============================

{"".join(state["arxiv_results"])}

==============================
💻 GITHUB IMPLEMENTATIONS
==============================

{github_text}
"""

    return {
        "combined_results": combined
    }


# ----------------------------------------------------
# Analysis
# ----------------------------------------------------
def analyze_node(state: ResearchState):

    print("🧠 Analyzing collected information...")

    prompt = f"""
You are a senior AI Research Analyst.

Research Question:
{state["question"]}

Below is information collected from multiple sources.

{state["combined_results"]}

Perform a detailed analysis.

Include:

1. Main findings
2. Latest industry developments
3. Latest research trends
4. Open-source implementations
5. Differences between sources
6. Future research directions

If two sources disagree,
mention both viewpoints.

Do NOT invent facts.
Use only the provided information.

Return only the analysis.
"""

    response = llm.invoke(prompt)

    return {
        "combined_results": response.content
    }


# ----------------------------------------------------
# Final Summary
# ----------------------------------------------------
def summarize_node(state: ResearchState):

    print("✍ Generating Deep Research Report...")

    prompt = f"""
You are an expert Research Assistant.

Research Question:

{state["question"]}

Analysis:

{state["combined_results"]}

Generate a professional markdown report.

The report MUST contain:

# Executive Summary

# Latest Developments

# Research Papers

For each paper include:
- Title
- Authors (if available)
- Summary

# Open Source Implementations

Mention GitHub repositories with:
- Repository name
- Description
- Stars
- Language

# Industry Applications

# Key Insights

# Future Research Directions

# Conclusion

At the end create:

# Sources Used

Include:
- 🌐 Latest Web
- 📚 Wikipedia
- 📄 ArXiv
- 💻 GitHub

Do not hallucinate information.
If information is unavailable, clearly state that.
"""

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }