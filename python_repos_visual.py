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

repo_links, repo_names, stars, hover_texts = [], [], [], []

# To summarize the top repos in a file.
print("\nFind the summary below")
for repo_dict in repo_dicts:
    # Turn repo names in to active links.
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_url)
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
    # Build hover texts
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner} <br /> {description}"
    hover_texts.append(hover_text)

# Make visualizations.

title = "Most-Starred Python Projects on GitHub"

lables = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links, y=stars, title=title, labels=lables, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20,)
fig.show()
