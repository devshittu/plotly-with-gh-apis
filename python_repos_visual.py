import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r=requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
# print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

repo_names, stars = [], []

# To summarize the top repos in a file.
print("\nFind the summary below")
for repo_dict in repo_dicts:
    print("\nSelected information about repository:")
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
    print("\n\n")

# Make visualizations.

title = "Most-Starred Python Projects on GitHub"

lables = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_names, y=stars, title=title, labels=lables)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20,)
fig.show()
