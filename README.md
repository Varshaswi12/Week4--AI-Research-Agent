# AI Deep Research Agent using LangGraph

An AI-powered Deep Research Agent built with LangGraph, Google Gemini, and multiple research sources to gather, analyze, and summarize information into a comprehensive research report.

The agent performs multi-step reasoning by collecting information from multiple sources, merging the results, analyzing them using Gemini, and generating a structured response.

---

## Features

-  Web Search using Tavily
-  Wikipedia Search
-  ArXiv Research Paper Search
-  GitHub Repository Search
-  AI-powered Analysis using Gemini
-  LangGraph StateGraph Workflow
-  Multi-step Reasoning
-  Streamlit Chat Interface
-  Research Summarization
-  Modular Node-Based Architecture

---

##Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini 2.5 Flash
- Tavily Search API
- Wikipedia API
- ArXiv API
- GitHub API (PyGithub)
- Streamlit

---

##Project Structure

```
week4-AI-Research-Agent
│
├── app.py
├── graph.py
├── nodes.py
├── state.py
├── tools.py
├── github_tools.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

##Workflow

```
User Question
      │
      ▼
Planner Node
      │
      ▼
Web Search (Tavily)
      │
      ▼
Wikipedia Search
      │
      ▼
ArXiv Search
      │
      ▼
GitHub Search
      │
      ▼
Merge Results
      │
      ▼
AI Analysis (Gemini)
      │
      ▼
Research Summary
```

---

##Installation

### Clone the repository

```bash
git clone https://github.com/Varshaswi12/Week4--AI-Research-Agent

cd Week4--AI-Research-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
GITHUB_TOKEN=your_github_token
```

---

## Run the Project

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## Example Research Query

```
Latest applications of AI in Healthcare
```

The AI agent will:

- Search the latest web articles
- Retrieve relevant Wikipedia information
- Find related ArXiv research papers
- Search GitHub repositories
- Analyze collected information
- Generate a professional research summary

---

## Future Improvements

- Conditional Routing using LangGraph
- Agent Memory
- Multi-Agent Collaboration
- PubMed Integration
- Semantic Scholar Integration
- OpenAlex Integration
- Export Report as PDF
- Citation Generation
- Deployment on Streamlit Cloud

---

## Learning Topics Covered

- AI Agents
- Agentic AI
- LangGraph Fundamentals
- StateGraph
- Nodes & Edges
- Tool Calling
- Multi-Step Reasoning
- Prompt Engineering
- LLM Integration
- Streamlit Deployment

---

## Author

Varshaswi



