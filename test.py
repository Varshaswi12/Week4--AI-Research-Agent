from github_tools import search_github

repos = search_github("AI healthcare")

for repo in repos:
    print(repo)