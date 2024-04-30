#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve this challenge"""

import requests
import sys

def get_commits(repo_name, owner_name):
    """Fetches and prints the 10 most recent commits for a GitHub repository.

    Args:
        repo_name (str): Name of the repository.
        owner_name (str): Name of the repository owner.
    """

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}  # Get 10 commits per request

    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print(f"Error: Request failed with status code {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python github_commits.py <repository_name> <owner_name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        get_commits(repo_name, owner_name)

