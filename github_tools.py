import os

from github import Github
from dotenv import load_dotenv

load_dotenv()


def search_github(query: str, max_results: int = 5):
    """
    Search GitHub repositories related to the query.
    """

    token = os.getenv("GITHUB_TOKEN")

    github = Github(token) if token else Github()

    try:
        repositories = github.search_repositories(
            query=query,
            sort="stars",
            order="desc"
        )

        results = []

        for repo in repositories[:max_results]:
            results.append({
                "name": repo.full_name,
                "description": repo.description,
                "stars": repo.stargazers_count,
                "url": repo.html_url,
                "language": repo.language
            })

        return results

    except Exception as e:
        return [{
            "error": str(e)
        }]