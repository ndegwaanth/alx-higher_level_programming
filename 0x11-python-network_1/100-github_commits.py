#!/usr/bin/python3
""" This script retrieves the 10 most recent commits from a specified
    repository by a given owner using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}
    headers = {'Accept': 'application/vnd.github.v3+json'}

    response = requests.get(url, params=params, headers=headers)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
